"""
Google Kick Start - Round F 2021 - Q3
Daniel Cortild - 18/09/2021
"""

import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import linprog
from scipy.spatial.distance import euclidean
from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def in_hull(points, x):
    n_points = len(points)
    n_dim = len(x)
    c = np.zeros(n_points)
    A = np.r_[points.T,np.ones((1,n_points))]
    b = np.r_[x, np.ones(1)]
    lp = linprog(c, A_eq=A, b_eq=b)
    return lp.success


for T in range(int(input())):
    N = int(input())

    WS = np.empty((N, 2))

    L = 100000000000000000

    for i in range(N):
        xw, yw = list(map(int, input().split())) 
        WS[i] = (xw, yw)

    XB, YB = list(map(int, input().split()))

    if N <= 2:
        print(f"Case #{T+1}: IMPOSSIBLE")
        continue

    for set in powerset(WS):
        if len(set) > 2 and in_hull(WS, (XB, YB)):
            hull = ConvexHull(WS)

            vertices = hull.vertices.tolist() + [hull.vertices[0]]
            perimeter = np.sum([euclidean(x, y) for x, y in zip(WS[vertices], WS[vertices][1:])])
            L = min(L, perimeter)

    print(f"Case #{T+1}: {perimeter}")
