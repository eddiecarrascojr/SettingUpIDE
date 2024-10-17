import fastai
import torch

import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KDTree

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:

        X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
        nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
        distances, indices = nbrs.kneighbors(X)

        print("Indices", indices,'\n')
        print("Distance", distances, '\n')

        nbrs.kneighbors_graph(X).toarray()


        X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
        kdt = KDTree(X, leaf_size=30, metric='euclidean')
        print("kdt", kdt.query(X, k=2, return_distance=False))

        data = {'Barton LLC': 109438.50,
                'Frami, Hills and Schmidt': 103569.59,
                'Fritsch, Russel and Anderson': 112214.71,
                'Jerde-Hilpert': 112591.43,
                'Keeling LLC': 100934.30,
                'Koepp Ltd': 103660.54,
                'Kulas Inc': 137351.96,
                'Trantow-Barrows': 123381.38,
                'White-Trantow': 135841.99,
                'Will LLC': 104437.60}
        group_data = list(data.values())
        group_names = list(data.keys())
        group_mean = np.mean(group_data)

        fig, ax = plt.subplots()
        ax.barh(group_names, group_data)
        fig.savefig('results.png', dpi=fig.dpi)

if __name__ == '__main__':
    main()