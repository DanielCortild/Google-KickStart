"""
Google Kick Start - Round A 2021 - Q2 [SOLVED]
Daniel Cortild - 21/03/2021
"""

import math

def getLfromForm(a, b):
  n = 0
  a, b = min(a,b), max(a,b)
  lL = min(math.floor(b/2), a) - 1
  sL = math.floor(a/2) - 1
  if lL < 0: lL = 0
  if sL < 0: sL = 0
  return lL + sL

def getSums(G):
  S = []
  for i in range(4):
    S.append([])
    for j in range(len(G)):
      S[i].append([])
      for k in range(len(G[j])):
        S[i][j].append(0)
  for r in range(len(G)):
    for c in range(len(G[r])):
      if r == 0:
        S[0][r][c] = G[r][c]
        S[2][len(G)-1-r][c] = G[len(G)-1-r][c]
      else:
        S[0][r][c] = G[r][c] * ( S[0][r-1][c] + 1 )
        S[2][len(G)-r-1][c] = G[len(G)-r-1][c] * ( S[2][len(G)-r][c] + 1 )
      if c == 0:
        S[1][r][c] = G[r][c]
        S[3][r][len(G[0])-1-c] = G[r][len(G[0])-1-c]
      else:
        S[1][r][c] = G[r][c] * ( S[1][r][c-1] + 1 )
        S[3][r][len(G[0])-1-c] = G[r][len(G[0])-1-c] * ( S[3][r][len(G[0])-c] + 1 )
  return S

def getNumberL(G):
  n = 0
  S = getSums(G)
  for i in range(len(G)):
    for j in range(len(G[i])):
        t, r, b, l = S[0][i][j], S[1][i][j], S[2][i][j], S[3][i][j]
        n += getLfromForm(t, r)
        n += getLfromForm(r, b)
        n += getLfromForm(b, l)
        n += getLfromForm(l, t)
  return n

for T in range(int(input())):
  R, C = list(map(int, input().split()))
  G = []
  for i in range(R):
    G.append(list(map(int, input().split())))

  print(f"Case #{T+1}: {getNumberL(G)}")