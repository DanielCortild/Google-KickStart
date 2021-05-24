"""
Google Kick Start - Round D 2020 - Q1 [SOLVED]
Daniel Cortild - 17/10/2020
"""

for t in range(int(input())):
  N = input()
  A = list(map(int, input().split()))

  nb = 0
  max = -1

  for i in range(len(A)):
    if A[i] > max:
      max = A[i]
      if i == len(A)-1 or A[i] > A[i+1]:
        nb += 1

  print("Case #{}: {}".format(t+1, nb))