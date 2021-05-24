"""
Google Kick Start - Round C 2021 - Q2 [SOLVED]
Daniel Cortild - 23/05/2021
"""

for T in range(int(input())):
  G = int(input())

  i = 1
  nb = 0
  while True:
    K = (2*G/i - i + 1)/2
    i += 1
    if K < 1:
      break
    if K == int(K):
      nb += 1

  print(f"Case #{T+1}: {nb}")