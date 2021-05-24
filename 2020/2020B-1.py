"""
Google Kick Start - Round B 2020 - Q1 [SOLVED]
Daniel Cortild - 17/10/2020
"""

for T in range(int(input())):
  N = int(input())
  H = list(map(int, input().split()))
  
  nb = 0

  for i in range(1, N-1):
    if H[i] > H[i-1] and H[i] > H[i+1]:
      nb += 1

  print("Case #{}: {}".format(T+1, nb))