"""
Google Kick Start - Round A 2020 - Q2 [SOLVED]
Daniel Cortild - 17/10/2020
"""

S = []
res = []

def dp(nb_rows, plates_left):
  if nb_rows == 0:
    if plates_left <= K:
      return S[0][plates_left]
    else:
      return 0
  if plates_left == 0:
    return 0
  
  if res[nb_rows][plates_left] == -1:
    res[nb_rows][plates_left] = max([ (dp(nb_rows-1, plates_left-k) + S[nb_rows][k]) for k in range(min(plates_left, K)+1)])
  return res[nb_rows][plates_left]
  

for T in range(int(input())):
  N, K, P = list(map(int, input().split()))
  A = []
  for k in range(N):
    A.append(list(map(int, input().split())))
  S = [[sum(a[0:i]) for i in range(K+1)] for a in A]
  res = [[-1 for j in range(P+1)] for i in range(N+1)]

  print("Case #{}: {}".format(T+1, dp(N-1, P)))