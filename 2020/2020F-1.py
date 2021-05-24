"""
Google Kick Start - Round F 2020 - Q1 [SOLVED]
Daniel Cortild - 17/10/2020
"""

import math

for t in range(int(input())):
  N, X = list(map(int, input().split()))
  A = list(map(int, input().split()))
  L = sorted( [(math.floor(A[n]/X), n) for n in range(N)], key = lambda x: (x[0], x[1]))
  print("Case #{}: {}".format(t+1, ' '.join(str(L[l][1]+1) for l in range(N))))
        