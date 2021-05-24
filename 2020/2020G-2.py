"""
Google Kick Start - Round G 2020 - Q2 [SOLVED]
Daniel Cortild - 09/11/2020
"""

for T in range(int(input())):
  N = int(input())
  C = []
  for i in range(N):
    C.append(list(map(int, input().split())))

  maxCoins = 0

  for i in range(-N+1, N-1):
    nbCoins = 0
    for j in range(2*N):
      if(C[i][j]):
        nbCoins += C[i-j][j]

    if nbCoins > maxCoins:
      maxCoins = nbCoins

  print("Case #{}: {}".format(T+1, maxCoins))