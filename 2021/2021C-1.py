"""
Google Kick Start - Round C 2021 - Q1 [SOLVED]
Daniel Cortild - 23/05/2021
"""

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
M = 10**9+7

for T in range(int(input())):
  N, K = list(map(int, input().split()))
  S = input()
  H = (N+1)//2
  nb = 0
  p = 1
  for i in range(H):
    nb += abc.index(S[H-i-1]) * p
    nb %= M
    p *= K  
    p %= M
  nb += (S[:H][::-1] < S[N//2:])
  nb %= M

  print(f"Case #{T+1}: {int(nb)}")