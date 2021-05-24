"""
Google Kick Start - Round A 2020 - Q3 [ONLY TEST 1]
Daniel Cortild - 17/10/2020
"""

import math

for T in range(int(input())):
  N, K = list(map(int, input().split()))
  M = list(map(int, input().split()))

  A = [M[i+1]-M[i] for i in range(N-1)]
  m = max(A)
  for i in range(N-1):
    if A[i] == m:
      A[i] = math.ceil(A[i]/2)
  newmax = max(A)
    
  print("Case #{}: {}".format(T+1, newmax))