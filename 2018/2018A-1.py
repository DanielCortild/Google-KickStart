"""
Google Kick Start - Round A 2018 - Q1 [RE]
Daniel Cortild - 17/10/2020
"""

for T in range(int(input())):
  N = input()
  while len(N):
    if int(N[0]) % 2 == 0:
      continue
    if 10**(len(N)+1)-int(N[1:]) <= int(N[1:])+1:
      sol += 10**(len(N)+1)-int(N[1:])
      break
    sol += int(N[1:])+1
    N =
  sol = 0


  print(f"Case #{T+1}: {sol}")