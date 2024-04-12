import numpy as np
import random

def write_img_file(img_file, data):
    with open(img_file, 'w') as f:
        for row in data:
            for element in row:
                f.write(str(element) + '\n')

def initialize_fire_layer(rows, columns):

    layer_data = np.zeros((rows, columns), dtype=int)
    i = random.randint(0, rows - 1)
    j = random.randint(0, columns - 1)
    layer_data[i][j] = 1

    return layer_data

def initialize_fuel_layer(rows, columns, cluster_len = 10):

    assert rows >= cluster_len and columns >= cluster_len, f'Error: insufficient cells for cluster_len = {cluster_len}'
    layer_data = np.zeros((rows, columns), dtype=int)
    #Assume 'cluster_len' clusters
    cluster_size_i = rows // cluster_len
    cluster_size_j = columns // cluster_len

    for clust_i in range(0, rows, cluster_size_i):
        for clust_j in range(0, columns, cluster_size_j):
            clust_density = random.randrange(1, 7, 2)
            #Assign FUEL layer's states
            for i in range(cluster_size_i):
                for j in range(cluster_size_j):
                    #Assert we don't go out of the grid
                    if clust_i + i < rows and clust_j + j < columns:
                        layer_data[clust_i+i][clust_j+j] = clust_density*random.randint(5, 10)

    #Add a fireproof diagonal path
    disp = random.randint(0, columns//2)
    for i in range(rows // 2):
        layer_data[i, i+disp] = 0

    return layer_data

def initialize_humidity_layer(rows, columns, cluster_len = 10):

    assert rows >= cluster_len and columns >= cluster_len, f'Error: insufficient cells for cluster_len = {cluster_len}'
    layer_data = np.zeros((rows, columns), dtype=int)
    #Assume 'cluster_len' clusters
    cluster_size_i = rows // cluster_len
    cluster_size_j = columns // cluster_len

    for clust_i in range(0, rows, cluster_size_i):
        for clust_j in range(0, columns, cluster_size_j):
            clust_density = random.randrange(1, 4)
            #Assign FUEL layer's states
            for i in range(cluster_size_i):
                for j in range(cluster_size_j):
                    #Assert we don't go out of the grid
                    if clust_i + i < rows and clust_j + j < columns:
                        layer_data[clust_i+i][clust_j+j] = clust_density*random.randint(2, 6)

    #Add random non-humid cells
    for _ in range((rows*columns) // 10):
        i = random.randint(0, rows - 1)
        j = random.randint(0, columns - 1)
        layer_data[i][j] = 0

    return layer_data