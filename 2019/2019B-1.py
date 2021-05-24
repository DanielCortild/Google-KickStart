"""
Google Kick Start - Round B 2019 - Q1 [ONLY TEST 1]
Daniel Cortild - 21/03/2021
"""

def couldBePalindrome(W):
  oddOccurence = ""
  for i in W:
    if W.count(i) % 2 == 1:
      if oddOccurence != "" and oddOccurence != i:
        return False
      oddOccurence = i
  return True

for T in range(int(input())):
  N, Q = list(map(int, input().split()))
  W = input()

  n = 0
  for _ in range(Q):
    L, R = list(map(int, input().split()))
    if couldBePalindrome(W[L-1:R]):
      n += 1


  print(f"Case #{T+1}: {n}")