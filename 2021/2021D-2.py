"""
Google Kick Start - Round D 2021 - Q2 [ONLY TEST 1]
Daniel Cortild - 11/07/2021
"""

import numpy as np
import heapq

for T in range(int(input())):
  N, C = list(map(int, input().split()))
  dic = {}

  L, R = np.empty(N), np.empty(N)

  for i in range(N):
    l, r = list(map(int, input().split()))
    L[i] = l
    R[i] = r

  l_min = int(np.min(L))
  r_max = int(np.max(R))

  x = np.zeros(r_max-l_min+1)

  for i in range(len(L)):
    x[int(L[i]+1-l_min)] += 1
    x[int(R[i]-l_min)] -= 1

  x = np.cumsum(x)
  cuts = int(N + np.sum(heapq.nlargest(C, x)))

  print(f"Case #{T+1}: {cuts}")