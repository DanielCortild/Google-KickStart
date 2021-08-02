"""
Google Kick Start - Round C 2021 - Q3 [SOLVED]
Daniel Cortild - 23/05/2021
"""

## PRELIMINARY CODE TO FIND THE STRATEGIES

import numpy as np

v = np.empty((60, 60, 60))
step = np.empty((60, 60, 60))

def computeExpVal(str, W, E):
  gain = 0
  r, p, s = 0, 0, 0
  i = 1
  for c in str:
    if c == 'R':
      if i == 1: gain += W / 3. + E / 3. 
      else: gain += W * p / (i - 1) + E * s / (i - 1)
      r += 1
    if c == 'P':
      if i == 1: gain += W / 3. + E / 3. 
      else: gain += W * s / (i - 1) + E * r / (i - 1)
      p += 1
    if c == 'S':
      if i == 1: gain += W / 3. + E / 3. 
      else: gain += W * r / (i - 1) + E * p / (i - 1)
      s += 1
    i += 1
  return gain


def getBestX(r, p, s, W, E):
  if not np.isnan(v[r][p][s]):
    return v[r][p][s]
  n = r + p + s
  l = [getBestX(r-1, p, s, W, E) + W * p / (n - 1) + E * s / (n - 1) if r > 0 else -100,
       getBestX(r, p-1, s, W, E) + W * s / (n - 1) + E * r / (n - 1) if p > 0 else -100,
       getBestX(r, p, s-1, W, E) + W * r / (n - 1) + E * p / (n - 1) if s > 0 else -100]
  i = np.argmax(l)
  step[r][p][s] = i
  v[r][p][s] = l[i]
  return v[r][p][s]

def getPath(r, p, s, path):
  if r + p + s == 0:
    return ''.join(path[::-1])
  ste = step[r][p][s]
  if ste == 0:
    path.append('R')
    return getPath(r-1, p, s, path)
  if ste == 1:
    path.append('P')
    return getPath(r, p-1, s, path)
  if ste == 2:
    path.append('S')
    return getPath(r, p, s-1, path)

def findBest(W, E):
  v.fill(None)
  step.fill(None)
  v[0][0][1], v[0][1][0], v[1][0][0] = [(W + E) / 3] * 3
  v[0][0][0] = 0
  step[0][0][1] = 2
  step[0][1][0] = 1
  step[1][0][0] = 0
  best = 0
  bi, bj = 0, 0
  for i in range(1, 61):
    for j in range(1, 61-i):
      b = getBestX(i, j, 60 - i - j, W, E)
      if b > best:
        best = b
        bi, bj = i, j
  return getPath(bi, bj, 60 - bi - bj, [])

# for _ in [0, 0.1, 0.5, 1]:
#   print(_, findBest(1, _))

## ONLY NEED CODE BELOW 

strategies = [
  "PRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSSSSSSPPPPPPPPPPPPPPPPPPPPPPP", # 0
  "SPPPPRRRRRRRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSSSSPPPPPPPPPPPPPPP", # 0.1
  "PRRSSSSPPPPPPPPRRRRRRRRRRRRRRRRSSSSSSSSSSSSSSSSSSSPPPPPPPPPP", # 0.5
  "SPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPR" # 1
]

T = int(input())
X = int(input())
for t in range(T):
  W, E = list(map(int, input().split()))
  if E == 0:
    strategy = strategies[0]
  elif W / E == 10:
    strategy = strategies[1]
  elif W / E == 2:
    strategy = strategies[2]
  elif W / E == 1:
    strategy = strategies[3]

  print(f"Case #{t+1}: {strategy}")

