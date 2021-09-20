"""
Google Kick Start - Round A 2018 - Q1 [SOLVED]
Daniel Cortild - 02/08/2021
"""

def lastGood(n):
  n_list = [int(c) for c in str(n)]
  for (i, k) in enumerate(n_list):
    if k % 2 == 1:
      n_list[i] -= 1
      for j in range(len(n_list[i+1:])):
        n_list[i + j + 1] = 8
      break
  return int(''.join(map(str, n_list)))

def nextGood(n):
  n_list = [int(c) for c in str(n)]
  start = 0
  for (i, k) in enumerate(n_list):
    if k % 2 == 1:
      if n_list[i] == 9:
        n_list[i] = 0
        ij = i
        while ij > 0 and n_list[ij-1] == 8:
          n_list[ij-1] = 0
          ij -= 1
        if ij == 0:
          start = 2
        else:
          n_list[ij-1] += 2
      else:
        n_list[i] += 1
      for j in range(len(n_list[i+1:])):
        n_list[i + j + 1] = 0
      break
  return int(''.join([str(start), *map(str, n_list)]))

for T in range(int(input())):
  N = int(input())
  
  A = lastGood(N)
  B = nextGood(N)

  print(f"Case #{T+1}: {min(N-A, B-N)}")