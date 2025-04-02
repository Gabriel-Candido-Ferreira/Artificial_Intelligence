import json
import os
import random
import matplotlib.pyplot as plt

CITY_FILE = "cities.json"
ROUTES_FILE = "best_routes.json"

def load_or_generate_cities(num_cities):
    if os.path.exists(CITY_FILE):
        with open(CITY_FILE, "r") as f:
            return json.load(f)
    else:
        cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_cities)]
        with open(CITY_FILE, "w") as f:
            json.dump(cities, f)
        return cities

def load_best_routes():
    if os.path.exists(ROUTES_FILE):
        with open(ROUTES_FILE, "r") as f:
            data = json.load(f)
            return [route for route in data if route["distance"] < 400]
    return []

def save_best_route(genes, distance):
    route_data = {
        "route": genes,
        "distance": distance
    }

    if os.path.exists(ROUTES_FILE):
        with open(ROUTES_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    if distance < 400:
        data.append(route_data)
        data = sorted(data, key=lambda r: r["distance"])[:5]

        with open(ROUTES_FILE, "w") as f:
            json.dump(data, f, indent=2)

def plot_results(distance_progress, best_genes, cities):
    x = [cities[i][0] for i in best_genes] + [cities[best_genes[0]][0]]
    y = [cities[i][1] for i in best_genes] + [cities[best_genes[0]][1]]

    plt.plot(distance_progress)
    plt.title("Evolução da Distância (TSP)")
    plt.xlabel("Geração")
    plt.ylabel("Distância da Melhor Rota")
    plt.grid(True)
    plt.show()