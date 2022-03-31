import math
import random


def calc_d(center, element):    # vypocet vzdialenosti
    x = center[0] - element[0]
    y = center[1] - element[1]

    return math.sqrt(x * x + y * y)


def gen_centers(data, k):   # init centrá
    centers = []
    old_clusters = []
    for i in range(k):
        center = random.choice(data)
        centers.append(center)
        old_clusters.append("X")

    return centers, old_clusters


def test(clusters, centers):    # testovanie
    failed = 0
    successful = 0

    for i in range(len(clusters)):
        distance = 0
        for point in clusters[i]:
            distance += calc_d(point, centers[i])
            
        if distance // len(clusters[i]) > 500:
            failed += 1

        else:
            successful += 1

    print("\nSuccessful clusters:", successful)
    print("Failed clusters:", failed)
