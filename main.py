import time
from kcentroids import *
from agglomerative import *
from kmedoids import *
from divisive import *
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from copy import deepcopy
sns.set_style("darkgrid")

k = int(input("Generated init points: "))       # zadavanie vstupu
k0 = int(input("How many clusters should be found? "))
all_points = []
hash_allpoints = []
dimension = 5000
data_number = int(input("Generated points: "))
offset = 0.02

for i in range(k0):     # generovanie začiatočných bodov
    x = random.randint(-dimension, dimension)
    y = random.randint(-dimension, dimension)
    new_point = [x, y]

    all_points.append(new_point)
    hash_allpoints.append(str(new_point))

i = 0
while i < data_number:      # generovanie ostatných bodov
    base = random.choice(all_points)
    if base[0] <= -dimension*0.98:
        x_offset = random.randint(-dimension-base[0], int(dimension*offset))

    elif base[0] >= dimension*0.98:
        x_offset = random.randint(-int(dimension*offset), dimension-base[0])

    else:
        x_offset = random.randint(-int(dimension*offset), int(dimension*offset))

    if base[1] <= -dimension*0.98:
        y_offset = random.randint(-dimension-base[1], int(dimension*offset))

    elif base[1] >= dimension*0.98:
        y_offset = random.randint(-int(dimension*offset), dimension-base[1])

    else:
        y_offset = random.randint(-int(dimension*offset), int(dimension*offset))

    new_point = [base[0] + x_offset, base[1] + y_offset]

    if str(new_point) in all_points:
        continue

    else:
        i += 1
        all_points.append(new_point)
        hash_allpoints.append(str(new_point))

fig, axes = plt.subplots(2, 2, figsize=(15, 8))
centers, old_clusters = gen_centers(all_points, k)  # vytvorenie centier inicializačných
print("-------------------------")
print("Kmeans centroid")
clusters_centroid, centers_centroid = k_centroids(all_points, k, deepcopy(centers), deepcopy(old_clusters)) # klastrovanie
#test(clusters_centroid, centers_centroid)

init_centers = np.array(centers)
initC_x, initC_y = init_centers.T

for cluster in clusters_centroid:   # vykreslovanie

    cluster = np.array(cluster)
    x, y = cluster.T

    sns.scatterplot(x=x, y=y, ax=axes[0][0])

centers = np.array(centers_centroid)
x, y = centers.T

sns.scatterplot(x=initC_x, y=initC_y, marker="x", color="brown", linewidth=2, s=40, ax=axes[0][0])
sns.scatterplot(x=x, y=y, marker="x", color="k", linewidth=2, s=40, ax=axes[0][0]).set_title("Centroids")

print("-------------------------")
print("Kmeans medoid")
clusters_medoid, centers_medoid = k_medoids(all_points, k, deepcopy(centers), deepcopy(old_clusters))   # klastrovanie
#test(clusters_medoid, centers_medoid)

for cluster in clusters_medoid:     # vykreslovanie

    cluster = np.array(cluster)
    x, y = cluster.T

    sns.scatterplot(x=x, y=y, ax=axes[0][1])

centers = np.array(centers_medoid)
x, y = centers.T
sns.scatterplot(x=initC_x, y=initC_y, marker="x", color="brown", linewidth=2, s=40, ax=axes[0][1])
sns.scatterplot(x=x, y=y, marker="x", color="k", linewidth=2, s=40, ax=axes[0][1]).set_title("Medoids")

print("-------------------------")
print("Divisions")
clursters_divisive, centers_devisive = k_divisions(deepcopy(all_points), k)     # klastrovanie
#test(clursters_divisive, centers_devisive)
for cluster in clursters_divisive:  # vykreslovanie

    cluster = np.array(cluster)
    x, y = cluster.T

    sns.scatterplot(x=x, y=y, ax=axes[1][0])

centers = np.array(centers_devisive)
x, y = centers.T
sns.scatterplot(x=x, y=y, marker="x", color="k", linewidth=2, s=40, ax=axes[1][0]).set_title("Divisive centroids")

print("-------------------------")
print("Agglomerative")
start = time.time()
clursters_agglomerative, centers_agglomerative = k_agglomerative(all_points, k)     # klastrovanie
#test(clursters_agglomerative, centers_agglomerative)
print(time.time()-start)
for cluster in clursters_agglomerative:     # vykreslovanie

    cluster = np.array(cluster)
    x, y = cluster.T

    sns.scatterplot(x=x, y=y, ax=axes[1][1])

centers = np.array(centers_agglomerative)
x, y = centers.T
sns.scatterplot(x=x, y=y, marker="x", color="k", linewidth=2, s=40, ax=axes[1][1]).set_title("Agglomerative centroids")
fig.show()
