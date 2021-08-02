"""
Google Kick Start - Round D 2021 - Q3 [SOLVES TEST 1]
Daniel Cortild - 11/07/2021
"""

maxDiff = 1001

for T in range(int(input())):
    N, M = list(map(int, input().split()))
    A = [0] * maxDiff
    for _ in range(N):
        a, b = list(map(int, input().split()))
        for d in range(a - 1, b):
            A[d] = 1
    S = list(map(int, input().split()))
    C = []
    for s in S:
        closestDist = maxDiff
        closestDiff = 0
        for d in range(maxDiff - 1):
            if A[d] == 1:
                if abs(s - d - 1) < closestDist:
                    closestDist = abs(s - d - 1)
                    closestDiff = d + 1
        C.append(closestDiff)
        A[closestDiff - 1] = 0

    print(f"Case #{T+1}: {' '.join(map(str, C))}")
