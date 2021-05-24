"""
Google Kick Start - Round A 2021 - Q3 [SOLVED]
Daniel Cortild - 23/03/2021
"""

import heapq

for T in range(int(input())):
  R, C = list(map(int, input().split()))
  G = []
  pq = []
  n = 0
  for i in range(R):
    G.append(list(map(int, input().split())))
  for i in range(R):
    for j in range(C):
      heapq.heappush(pq, (-G[i][j], i, j))
  while pq:
    v, i, j = heapq.heappop(pq)
    v = -v
    if G[i][j] <= v: 
      for x, y in ((i-1, j), (i, j-1), (i+1, j), (i, j+1)):
        if 0 <= x < R and 0 <= y < C and G[x][y] < v-1:
          n += v - 1 - G[x][y]
          G[x][y] = v-1
          heapq.heappush(pq, (-G[x][y], x, y))

  print(f"Case #{T+1}: {n}")