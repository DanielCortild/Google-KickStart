"""
Google Kick Start - Round B 2020 - Q2 [SOLVED]
Daniel Cortild - 21/11/2020
"""

import math

for T in range(int(input())):
  N, D = list(map(int, input().split()))
  X = list(map(int, input().split()))
  
  for i in range(N-1, -1, -1):
    D = math.floor(D/X[i])*X[i]

  print("Case #{}: {}".format(T+1, D))