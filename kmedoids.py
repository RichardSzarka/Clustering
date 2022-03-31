import sys

from other import *


def calc_centers(clusters):     # najdi medoid
    centers = []
    for cluster in clusters:
        minimum = 9999999
        medoid = None
        for element1 in cluster:
            sumarry = 0
            for element2 in cluster:
                sumarry += calc_d(element1, element2)
            if minimum > sumarry:
                minimum = sumarry
                medoid = element1

        centers.append(medoid)
    return centers


def make_clusters(data, centers, k):    # vytvor clastre
    clusters = []
    for i in range(k):
        clusters.append([])

    index = -1
    for element in data:
        i = 0
        distance = 10000
        for center in centers:
            d = calc_d(center, element)
            if d < distance:
                index = i
                distance = d
            i += 1

        clusters[index].append(element)

    return clusters


def k_medoids(data, k, centers, old_clusters):

    gen = 0
    while True:
        found = False
        clusters = make_clusters(data, centers, k)  # vytvor klastre

        for i in range(len(clusters)):      # zisti ci su zhodne so starými
            if str(clusters[i]) != old_clusters[i]:
                found = True
                break

        if found is False:  # ak neboli
            break

        old_clusters = []
        for cluster in clusters:
            old_clusters.append(str(cluster))

        centers = calc_centers(clusters)    # vypocitaj centra a opakuj

        gen += 1
        sys.stdout.write("\r"+str(gen))

    return clusters, centers
