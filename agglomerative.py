import sys

from other import *


def make_matrix(data):  # vytváranie matice
    matrix = []
    centroids = []

    for element1 in data:
        row = []
        for element2 in data:
            if element2 == element1:
                row.append(999999)  # miesto 0
            else:
                row.append(calc_d(element1[0], element2[0]))
        centroids.append(element1[0])
        matrix.append(row)

    return matrix, centroids


def minimum_distance(matrix):   # najdenie minima v matici
    minimum = 999999
    row_ans = 0
    column_ans = 0
    for row in range(len(matrix)):
        local_min = min(matrix[row])
        if local_min < minimum:
            minimum = local_min
            row_ans = row
            column_ans = matrix[row].index(local_min)

    return row_ans, column_ans


def calc_centroid(cluster):     # vypočitavanie centroidu
    x = 0
    y = 0
    for element in cluster:
        x += element[0]
        y += element[1]
    centroid = [x // len(cluster), y // len(cluster)]

    return centroid


def merge(data, matrix, centroids, cluster1, cluster2):     # spojenie dvoch klastrov
    data[cluster1].extend(data[cluster2])

    data.pop(cluster2)

    del matrix[cluster2]
    del centroids[cluster2]

    centroids[cluster1] = calc_centroid(data[cluster1])
    new_row = []

    for i in range(len(matrix)):    # uprava stlpcov
        del matrix[i][cluster2]
        if i == cluster1:
            distance = 999999
        else:
            distance = calc_d(centroids[cluster1], centroids[i])
        matrix[i][cluster1] = distance
        new_row.append(distance)

    matrix[cluster1] = new_row      # uprava riadkov
    return data, matrix


def tidy_data(data):    # vytvorenie kazdeho bodu na klaster
    array = [["x"]]

    for element in data:
        array.append([element])

    array.pop(0)
    return array


def k_agglomerative(data, k):
    data = tidy_data(data)
    print("making matrix")
    matrix, centroids = make_matrix(data)

    while len(matrix) != k:     # opakuj kým nemáš potrebný počet klastrov
        sys.stdout.write("\r"+str(len(matrix)))
        cluster1, cluster2 = minimum_distance(matrix)   # nájdi najmenšiu vzdialenosť
        data, matrix = merge(data, matrix, centroids, cluster1, cluster2)   # spoj

    sys.stdout.write("\r" + str(len(matrix)))
    return data, centroids
