"""
Google Kick Start - Round B 2019 - Q1 [SOLVED]
Daniel Cortild - 03/08/2021
"""

import numpy as np

def getPrefixSums(W):
  prefixSums = []
  prefixSum = np.zeros(26)
  for i in range(len(W)):
    prefixSums.append(prefixSum.copy())
    prefixSum[ord(W[i]) - ord('A')] += 1
  prefixSums.append(prefixSum.copy())
  return prefixSums

def getList(W, n):
  l = np.zeros(26)
  for i in range(n):
    l[ord(W[i]) - ord('A')] += 1
  return l

def canBePalindrome(W, L, R, prefixSums):
  Ll = prefixSums[L-1]
  Rl = prefixSums[R]
  diff_l = (Rl - Ll) % 2
  if (R - L + 1) % 2 == 0:
    return not np.any(diff_l)
  return np.count_nonzero(diff_l == 1) == 1

for T in range(int(input())):
  N, Q = list(map(int, input().split()))
  W = input()
  n = 0
  prefixSums = getPrefixSums(W)
  for _ in range(Q):
    L, R = list(map(int, input().split()))
    if canBePalindrome(W, L, R, prefixSums):
      n += 1

  print(f"Case #{T+1}: {n}")