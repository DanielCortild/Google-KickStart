"""
Google Kick Start - Round B 2021 - Q2 [NOT SOLVED]
Daniel Cortild - 19/04/2021
"""

for T in range(int(input())):
  N = int(input())
  A = list(map(int, input().split()))

  D = [A[i]-A[i-1] for i in range(1, N)]
  m = 0
  for i in range(len(D)-1):
    l = 1
    joker = 1
    skip = 0
    for j in range(i+1, len(D)):
      if skip:
        skip = 0
        continue
      if D[j] == D[i]:
        l += 1
      elif j != len(D)-1 and D[j]+D[j+1] == 2*D[i]:
        if joker == 1:
          joker = 0
          l += 2
          skip = 1
        else:
          break
      elif j == len(D)-1 and joker == 1:
        l += 1
    m = max(l, m)

  print(f"Case #{T+1}: {m+1}")