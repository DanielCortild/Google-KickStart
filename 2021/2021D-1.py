"""
Google Kick Start - Round D 2021 - Q1 [SOLVED]
Daniel Cortild - 11/07/2021
"""

def nbArith(G, a):
  nb = 0
  if G[0][0] - G[0][1] == G[0][1] - G[0][2]: nb += 1
  if G[1][0] - a == a - G[1][2]: nb += 1
  if G[2][0] - G[2][1] == G[2][1] - G[2][2]: nb += 1

  if G[0][0] - G[1][0] == G[1][0] - G[2][0]: nb += 1
  if G[0][1] - a == a - G[2][1]: nb += 1
  if G[0][2] - G[1][2] == G[1][2] - G[2][2]: nb += 1

  if G[0][0] - a == a - G[2][2]: nb += 1
  if G[0][2] - a == a - G[2][0]: nb += 1
  return nb

def possArith(G):
  return [
    ( G[1][0] + G[1][2] ) / 2,
    ( G[0][1] + G[2][1] ) / 2,
    ( G[0][0] + G[2][2] ) / 2,
    ( G[2][0] + G[0][2] ) / 2
    ]

for T in range(int(input())):
  G = []
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  c = list(map(int, input().split()))
  b = [b[0], '_', b[1]]
  G = [a, b, c]
  
  m = 0
  for p in possArith(G):
    if int(p) == p:
      n = nbArith(G, p)
      if n > m:
        m = n

  print(f"Case #{T+1}: {m}")