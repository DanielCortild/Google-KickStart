"""
Google Kick Start - Round C 2020 - Q1 [SOLVED]
Daniel Cortild - 17/10/2020
"""

for t in range(int(input())):
  N, K = list(map(int, input().split()))
  A = list(map(int, input().split()))

  nb = 0
  l = 0

  for i in range(len(A)):
    if A[i] == K-l:
      l += 1
    elif A[i] == K:
      l = 1
    else:
      l = 0

    if l == K:
      l = 0
      nb += 1

  print("Case #{}: {}".format(t+1, nb))