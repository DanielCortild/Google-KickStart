"""
Google Kick Start - Round A 2019 - Q1 [SOLVED]
Daniel Cortild - 19/03/2021
"""

def getTrainingHours (S, N, P): 
  s = P*S[P-1]-sum(S[:P])
  m = s
  for i in range(1, N-P+1):
    s += S[i-1]+(P-1)*S[i-1+P]-P*S[i-2+P]
    m = min(m, s)
  return m

for T in range(int(input())):
  N, P = list(map(int, input().split()))
  S = sorted(list(map(int, input().split())))

  trainingHours = getTrainingHours(S, N, P)

  print(f"Case #{T+1}: {trainingHours}")