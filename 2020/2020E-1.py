"""
Google Kick Start - Round E 2020 - Q1
Daniel Cortild - 17/10/2020
"""

for t in range(int(input())):
  N = int(input())
  A = list(map(int, input().split()))
  B = [A[i+1]-A[i] for i in range(len(A)-1)]

  max = 0
  current = 0

  for b in B:
    if b == last:
      current += 1
    else:
      last = b
      if current > max:
        max = current
      current = 1
    
  if current > max:
    max = current
  
  print("Case #{}: {}".format(t+1, max+1))