"""
Google Kick Start - Round H 2020 - Q1 [SOLVED]
Daniel Cortild - 15/11/2020
"""

for T in range(int(input())):
  N, K, S = map(int, input().split())
  sol = min(K+N, N+2*(K-S))
  print("Case #{}: {}".format(T+1, sol))