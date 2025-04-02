import random
import math
import json
import os
from utils import (
    load_or_generate_cities,
    load_best_routes,
    save_best_route,
    plot_results
)

NUM_CITIES = 20
POPULATION_SIZE = 1000
GENERATIONS = 100
BASE_MUTATION_RATE = 0.01
OPTIMAL_DISTANCE = 300
OPTIMAL_FITNESS = 1 / OPTIMAL_DISTANCE
USE_ELITE = True

cities = load_or_generate_cities(NUM_CITIES)
cities = [tuple(city) for city in cities]

def euclidean_distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

distances = [[euclidean_distance(c1, c2) for c2 in cities] for c1 in cities]

class Individual:
    def __init__(self, genes=None):
        if genes:
            self.genes = genes
        else:
            self.genes = list(range(NUM_CITIES))
            random.shuffle(self.genes)
        self.fitness = self.evaluate_fitness()

    def evaluate_fitness(self):
        total_distance = 0
        for i in range(NUM_CITIES):
            from_city = self.genes[i]
            to_city = self.genes[(i + 1) % NUM_CITIES]
            total_distance += distances[from_city][to_city]
        return 1 / total_distance

def pmx_crossover(parent1, parent2):
    size = len(parent1.genes)
    start, end = sorted(random.sample(range(size), 2))
    
    child_genes = [None] * size
    child_genes[start:end] = parent1.genes[start:end]

    mapping = {p1: p2 for p1, p2 in zip(parent1.genes[start:end], parent2.genes[start:end])}

    for i in range(size):
        if child_genes[i] is None:
            gene = parent2.genes[i]
            while gene in mapping:
                gene = mapping[gene]
            child_genes[i] = gene

    return Individual(child_genes)

def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(NUM_CITIES), 2)
        individual.genes[i], individual.genes[j] = individual.genes[j], individual.genes[i]
        individual.fitness = individual.evaluate_fitness()

def scaled_fitness(population):
    min_fit = min(ind.fitness for ind in population)
    return [(ind.fitness - min_fit + 1e-6) for ind in population]

def roulette_wheel_selection(population):
    scaled_fitnesses = scaled_fitness(population)
    total_fitness = sum(scaled_fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for ind, fit in zip(population, scaled_fitnesses):
        current += fit
        if current >= pick:
            return ind

distance_progress = []
population = [Individual() for _ in range(POPULATION_SIZE)]
best_individual = max(population, key=lambda ind: ind.fitness)
best_distance = 1 / best_individual.fitness
stagnant_generations = 0
elite_pool = load_best_routes() if USE_ELITE else []

for generation in range(GENERATIONS):
    new_population = []
    
    mutation_rate = min(0.5, BASE_MUTATION_RATE * (1 + stagnant_generations / 10))
    
    elite_size = int(0.05 * POPULATION_SIZE)
    elite_pool = sorted(population, key=lambda ind: ind.fitness, reverse=True)[:elite_size]
    new_population.extend(elite_pool)
    
    while len(new_population) < POPULATION_SIZE - 2:
        parent1 = roulette_wheel_selection(population)
        parent2 = roulette_wheel_selection(population)
        if parent1 == parent2:
            pass
        child = pmx_crossover(parent1, parent2)
        mutate(child, mutation_rate)
        new_population.append(child)
    
    new_population.append(Individual())
    new_population.append(Individual())
    
    if stagnant_generations >= 15:
        num_random = POPULATION_SIZE // 5
        new_population[-num_random:] = [Individual() for _ in range(num_random)]
        stagnant_generations = 0
    
    population = new_population
    current_best = max(population, key=lambda ind: ind.fitness)
    current_distance = 1 / current_best.fitness
    
    if current_distance < best_distance:
        best_individual = current_best
        best_distance = current_distance
        stagnant_generations = 0
    else:
        stagnant_generations += 1
    
    distance_progress.append(best_distance)
    print(f"Geração {generation}: Melhor Rota = {best_individual.genes} Melhor distância = {best_distance:.2f}")
    
    if current_best.fitness >= OPTIMAL_FITNESS:
        print(f"\nSolução satisfatória atingida na geração {generation} com distância {current_distance:.2f}")
        break

print("\nMelhor rota encontrada:")
print(best_individual.genes)
print(f"Distância total: {best_distance:.2f}")

save_best_route(best_individual.genes, best_distance)
plot_results(distance_progress, best_individual.genes, cities)
