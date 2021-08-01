"""
Google Kick Start - Round B 2021 - Q2 [NOT SOLVED]
Daniel Cortild - 19/04/2021
"""

for T in range(int(input())):
  N = int(input())
  A = list(map(int, input().split()))

  D = [A[i]-A[i-1] for i in range(1, N)]
  d = {}

  for i in range(len(D)):
    if i > 0 and D[i] == D[first]:
      d[first] += 1
    else:
      first = i
      d[first] = 1

  max_length = 0
  for k in d.keys():
    length = d[k]
    mlen = length

    if k + length < len(D): # Can add at least one at end
      mlen = length + 1
    if k > 0: # Can add at least one at start
      mlen = length + 1

    if k > 1 and D[k - 2] + D[k - 1] == 2 * D[k]: # Change two before
      mlen = length + 2

    try:
      if D[k + length] + D[k + length + 1] == 2 * D[k]: # Change two afterwards
        mlen = length + 2
        if k + length + 2 in d.keys() and D[k + length + 2] == D[k]: # Can append to the one afterwards
          mlen += d[k + length + 2]
    except:
      pass
   
    if mlen > max_length:
      max_length = mlen
      mi = k

  print(f"Case #{T+1}: {max_length + 1}")