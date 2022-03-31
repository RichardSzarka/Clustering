import sys

from other import *


def calc_centers(clusters, centers):    # vypocet centroidov
    for i in range(len(clusters)):
        x = 0
        y = 0
        for element in clusters[i]:
            x += element[0]
            y += element[1]
        if len(clusters[i]) != 0:
            centers[i] = [x // len(clusters[i]), y // len(clusters[i])]

    return centers


def make_clusters(data, centers, k):    # vytvaranie klasterov
    clusters = []
    for i in range(k):
        clusters.append([])

    index = -1
    for element in data:
        i = 0
        distance = 999999
        for center in centers:
            d = calc_d(center, element)
            if d < distance:
                index = i
                distance = d
            i += 1

        clusters[index].append(element)

    return clusters

# hlavna funkcia
def k_centroids(data, k, centers, old_clusters):

    gen = 0
    while True:
        found = False
        clusters = make_clusters(data, centers, k)  # vytvor clustre
        for i in range(len(clusters)):  # cyklus kontroluje či sú
            if str(clusters[i]) != old_clusters[i]: # sú rozdielne
                found = True
                break

        if found is False:  # ak boli rovnaké skonči
            break

        old_clusters = []
        for cluster in clusters:    # vytvor hashe starých clusterov
            old_clusters.append(str(cluster))

        centers = calc_centers(clusters, centers)   # vypočítaj nové centroidy

        gen += 1
        sys.stdout.write("\r"+str(gen))

    return clusters, centers
