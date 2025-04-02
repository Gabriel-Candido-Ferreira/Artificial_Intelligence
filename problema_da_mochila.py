import random
import matplotlib.pyplot as plt

items = {
    1: 2,   2: 10,  3: 8,   4: 5,   5: 3,  
    6: 12,  7: 2,   8: 6,   9: 15,  10: 7,  
    11: 4,  12: 9,  13: 1,  14: 11, 15: 14,
    16: 13, 17: 3,  18: 5,  19: 4,  20: 8, 30: 3
}

max_weight = 20
optimal_fitness = 40
item_keys = list(items.keys())
item_values = list(items.values())
num_items = len(items)
fitness_progress = []

class Individual:
    def __init__(self, genes=None):
        self.genes = genes if genes else [random.randint(0, 1) for _ in range(num_items)]
        self.fitness = self.evaluate_fitness()

    def evaluate_fitness(self):
        weight, value = 0, 0
        for i, selected in enumerate(self.genes):
            if selected:
                weight += item_keys[i]
                value += item_values[i]
        return value if weight <= max_weight else 0

def crossover(parent1, parent2, mutation_rate):
    crossover_point = random.randint(1, num_items - 1)
    
    child1_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
    child2_genes = parent2.genes[:crossover_point] + parent1.genes[crossover_point:]
    
    for genes in (child1_genes, child2_genes):
        if random.random() < mutation_rate:
            mutate_index = random.randint(0, num_items - 1)
            genes[mutate_index] = 1 - genes[mutate_index]
    
    return Individual(child1_genes), Individual(child2_genes)

def tournament_selection(population):
    return max(random.sample(population, 2), key=lambda ind: ind.fitness)

population_size = 1000 
population = [Individual() for _ in range(population_size)]
generation = 0

current_best_coeff = 0.0
current_best_fit = 0.0
current_best_genes = [0 for _ in range(num_items)]

while True:
    best_individual = max(population, key=lambda ind: ind.fitness)

    if best_individual.fitness / optimal_fitness > current_best_coeff:
        current_best_coeff = best_individual.fitness / optimal_fitness
        current_best_genes = best_individual.genes[:]
        current_best_fit = best_individual.fitness

    print(f"Geração {generation}: Melhor fitness: {int(current_best_fit)} | Avaliação percentual: {(current_best_coeff * 100):.1f}%")
    fitness_progress.append(current_best_fit)

    if best_individual.fitness >= optimal_fitness:
        break

    mutation_rate = max(0.01, 0.1 / (1 + generation))

    new_population = [best_individual]
    while len(new_population) < population_size:
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        child1, child2 = crossover(parent1, parent2, mutation_rate)
        new_population.extend([child1, child2])

    population = new_population[:population_size]
    generation += 1

(current_best_genes, current_best_fit, generation)


print("\nMelhor combinação encontrada:")
total_weight = 0
for i, selected in enumerate(current_best_genes):
    if selected:
        item_id = item_keys[i]
        item_value = item_values[i]
        total_weight += item_id
        print(f"Item (peso={item_id}, valor={item_value})")

print(f"Peso total: {total_weight}")
print(f"Valor total: {current_best_fit}")
print(f"Gerações até solução ótima: {generation}")

plt.plot(fitness_progress)
plt.title("Evolução do Fitness")
plt.xlabel("Geração")
plt.ylabel("Melhor Fitness")
plt.grid(True)
plt.show()