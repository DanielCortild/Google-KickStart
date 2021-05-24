"""
Google Kick Start - Round B 2021 - Q3 [SOLVED]
Daniel Cortild - 19/04/2021
"""

def isPrime(n):
  if n == 2: return True
  if n < 2 or n % 2 == 0: return False
  return not any(n % i == 0 for i in range(3, int(n**.5) + 1, 2))

def nextPrime(n):
  while not isPrime(n):
    n += 1
  return n

def prevPrime(n):
  while not isPrime(n):
    n -= 1
  return n

for T in range(int(input())):
  Z = int(input())
  pP = prevPrime(int(Z**.5))
  nP = nextPrime(int(Z**.5)+1)
  if nP*pP > Z:
    nP = pP
    pP = prevPrime(pP-1)
  print(f"Case #{T+1}: {nP*pP}")