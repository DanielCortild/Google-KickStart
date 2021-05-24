"""
Google Kick Start - Round A 2020 - Q1 [SOLVED]
Daniel Cortild - 17/10/2020
"""

for T in range(int(input())):
  N, B = list(map(int, input().split()))
  A = sorted(list(map(int, input().split())))

  total_prize = 0
  nb = 0

  for i in range(N):
    if total_prize + A[i] <= B:
      total_prize = total_prize + A[i]
      nb = i+1

  print("Case #{}: {}".format(T+1, nb))