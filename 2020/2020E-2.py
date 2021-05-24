"""
Google Kick Start - Round E 2020 - Q2 [SOLVED]
Daniel Cortild - 17/10/2020
"""

for t in range(int(input())):
  N, A, B, C = list(map(int, input().split()))

  if A+B-C>N or ( A+B-C == 1 and N >= 2 ):
    S = "IMPOSSIBLE"
  else:
    S = []

    if N == 1:
      S = "1"

    elif N == 2:
      if C == 1:
        if A == 1 and B == 2:
          S = "2 1"
        elif A == 2 and B == 1:
          S = "1 2"
        else:
          S = "IMPOSSIBLE"
      elif C == 2:
        S = "2 2"

    elif N >= 3:
      for i in range(0, A-C):
        S.append(2)
      for i in range(0, C):
        S.append(3)
      for i in range(0, B-C):
        S.append(2)
      for i in range(0, N-A-B+C):
        S.insert(1, 1)
      S = ' '.join(str(s) for s in S)



  print("Case #{}: {}".format(t+1, S))