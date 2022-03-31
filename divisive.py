import sys

from other import *


def find_largestD(clusters):    # najvačší distance
    cluster_ans = 0
    element1 = 0
    maximum = 0

    for cluster in range(len(clusters)):
        d = 0
        for e1 in range(len(clusters[cluster])):
            for e2 in range(len(clusters[cluster])):
                d += calc_d(clusters[cluster][e1], clusters[cluster][e2])
            if d > maximum:
                maximum = d
                cluster_ans = cluster
                element1 = e1

    return cluster_ans, element1


def calc_centroid(cluster):     # vypocitaj centroid
    x = 0
    y = 0
    for e in cluster:
        x += e[0]
        y += e[1]

    centroid = [x // len(cluster), y // len(cluster)]

    return centroid


def divide(clusters, clstr, e1):    # rozdel klaster
    cluster = clusters[clstr]
    new_cluster = [cluster[e1]]

    clusters.append(new_cluster)
    cluster.pop(e1)
    centroid = calc_centroid(cluster)

    elem_totransfer = []
    for e in range(len(cluster)):   # prirad ku novemu alebo nechaj v starom
        if calc_d(cluster[e], centroid) <= calc_d(cluster[e], new_cluster[0]):
            continue
        else:
            new_cluster.append(cluster[e])
            elem_totransfer.append(e)

    elem_totransfer = sorted(elem_totransfer, reverse=True)     # vymaz zo stareho
    for e in elem_totransfer:
        cluster.pop(e)
    return clusters


def k_divisions(data, k):
    clusters = [data]

    while len(clusters) != k:   # kým nie je počet klastrov K

        sys.stdout.write("\r"+str(len(clusters)))
        cluster_todivide, e1 = find_largestD(clusters)   # najdi najviac disproporčný bod
        clusters = divide(clusters, cluster_todivide, e1)   # vytvor nový cluster

    sys.stdout.write("\r" + str(len(clusters)))
    centers = []
    for cluster in clusters:
        centers.append(calc_centroid(cluster))

    return clusters, centers
