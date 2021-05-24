"""
Google Kick Start - Round F 2020 - Q2 [SOLVED]
Daniel Cortild - 17/10/2020
"""

import math

for T in range(int(input())):
  N, K = list(map(int, input().split()))
  I = []
  for n in range(N):
    A = list(map(int, input().split()))
    I.append((A[0], A[1]))
  I = sorted(I, key = lambda x: x[0])
  nb = 0

  lastHarvested = 0

  for J in I:
    if lastHarvested < J[1]:
      t = max(lastHarvested, J[0])
      lastHarvested = t + math.ceil((J[1]-t)/K)*K
      nb += math.ceil((J[1]-t)/K)

  print("Case #{}: {}".format(T+1, nb))