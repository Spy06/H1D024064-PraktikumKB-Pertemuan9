import random

def roulette_wheel_selection(populasi, fitness_populasi):
    total_fitness = sum(fitness_populasi)
    if total_fitness == 0:
        idx = random.randrange(len(populasi))
        return populasi[idx], idx  

    probabilitas = [fitness / total_fitness for fitness in fitness_populasi]
    kumulatif_prob = []
    kumulatif = 0
    for p in probabilitas:
        kumulatif += p
        kumulatif_prob.append(kumulatif)

    r = random.random()
    for i, kum_prob in enumerate(kumulatif_prob):
        if r <= kum_prob:
            return populasi[i], i  

    return populasi[-1], len(populasi)-1  

def tournament_selection(populasi, fitness_populasi, k=3):
    if len(populasi) < k:
        k = len(populasi)
    peserta_indices = random.sample(range(len(populasi)), k)
    peserta = [(populasi[i], fitness_populasi[i], i) for i in peserta_indices]
    peserta.sort(key=lambda x: x[1], reverse=True)
    return peserta[0][0], peserta[0][2]  

if __name__ == "__main__":
    populasi_awal = ['individu1', 'individu2', 'individu3', 'individu4']
    fitness_populasi = [10, 20, 30, 40]

    available_populasi = populasi_awal.copy()
    available_fitness = fitness_populasi.copy()

    parent1, idx1 = roulette_wheel_selection(available_populasi, available_fitness)

    del available_populasi[idx1]
    del available_fitness[idx1]

    parent2, idx2 = tournament_selection(available_populasi, available_fitness)

    del available_populasi[idx2]
    del available_fitness[idx2]

    print("\nParent Terpilih:")
    print(f"Parent 1: {parent1}")
    print(f"Parent 2: {parent2}")