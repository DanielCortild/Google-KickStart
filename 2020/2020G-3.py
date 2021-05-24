"""
Google Kick Start - Round G 2020 - Q3 [ONLY TEST 1]
Daniel Cortild - 17/10/2020
"""

import math

res = [[-1 for i in range(5001)] for n in range(5001)]

def coef(i, n):
  if n == 1 or i < 0 or i > n:
    return 0
  if(res[i][n] == -1):
    first_last = 0
    if i == 0 or i == n-1:
      first_last = 1
    else:
      first_last = 2
    res[i][n] = i*coef(i-1, n-1)+(n-i-1)*coef(i, n-1)+first_last*math.factorial(n-2)
  return res[i][n]

def f(A):
  tot = 0
  for i in range(len(A)):
    tot += A[i]*coef(i, len(A))
  return tot

for T in range(int(input())):
  N = int(input())
  A = list(map(int, input().split()))
  print("Case #{}: {}".format(T+1, f(A)/(math.factorial(len(A)-1))))