"""
Google Kick Start - Round B 2018 - Q1 [SOLVED]
Daniel Cortild - 03/08/2021
"""

def nbLegalLess(n):
  nb = 0
  for l in range(n % 10 + 1):
    nb += isLegal(n - l)
  n -= n % 10
  n_base9 = sum([9 ** i * a for (i, a) in enumerate(list(map(int, [c for c in str(n)]))[::-1])])
  return nb + n_base9 * 8 // 9


def isLegal(n):
  if n % 9 == 0:
    return 0
  n_list = [c for c in str(n)]
  for k in n_list:
    if k == '9':
      return 0
  return 1

for T in range(int(input())):
  F, L = map(int, input().split())
  print(f"Case #{T+1}: {nbLegalLess(L) - nbLegalLess(F) + 1}")