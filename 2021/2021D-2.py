"""
Google Kick Start - Round D 2021 - Q2 [SOLVED]
Daniel Cortild - 11/07/2021
"""

for T in range(int(input())):
    N, C = list(map(int, input().split()))

    M = {}

    for i in range(N):
        L, R = list(map(int, input().split()))
        if L + 1 not in M:
            M[L + 1] = 1
        else:
            M[L + 1] += 1
        if R not in M:
            M[R] = -1
        else:
            M[R] -= 1

    K = sorted(M.keys())

    nb_cuts = 0
    key_prev, key_curr = K[0:2]
    A = {}

    for i in range(1, len(K)):
        key_prev, key_curr = K[i - 1:i + 1]
        nb_cuts += M[key_prev]
        if nb_cuts not in A:
            A[nb_cuts] = 0
        A[nb_cuts] += key_curr - key_prev

    cuts = N
    A2 = list(sorted(A.keys()))[::-1]
    idx = 0

    while C > 0 and idx < len(A2):
        mi = A2[idx]
        cuts += min(C, A[mi]) * mi
        C -= min(C, A[mi])
        idx += 1

    print(f"Case #{T+1}: {cuts}")
