"""
Google Kick Start - Round D 2021 - Q3 [NOT SOLVED]
Daniel Cortild - 11/07/2021
"""

import numpy as np

def getClosest(A, B, G, s):
    a = np.argmin(abs(A - s))
    b = np.argmin(abs(B - s))
    # print("s=", s, "a=", a, "b=", b, "A=", A, "B=", B, "abs(B-s)=", abs(B-s))
    if A[a] <= s <= B[b]:
        s1 = s
        s2 = s
        while s1 in G and s1 <= B[b]:
            s1 += 1
        while s2 in G and s2 >= A[a]:
            s2 -= 1
        s1good = False
        s2good = False
        if s1 not in G and s1 <= B[b]:
            s1good = True
        if s2 not in G and s2 >= A[a]:
            s2good = True
        if not s1good and s2good:
            G.append(s2)
            return A, B, G, s2
        elif not s2good and s1good:
            G.append(s1)
            return A, B, G, s1
        elif s1good and s2good:
            if abs(s2 - s) <= abs(s1 - s):
                G.append(s2)
                return A, B, G, s2
            else:
                G.append(s1)
                return A, B, G, s1
        else:
            A = np.delete(A, a)
            B = np.delete(B, b)
            return getClosest(A, B, G, s)
    else:
        # if a == b:
        #   b += 1
        if abs(s - B[b]) <= abs(s - A[a]):
            sc = B[b]
            if B[b] - 1 < A[a] and a == b:
                A = np.delete(A, a)
                B = np.delete(B, b)
            else:
                B[b] -= 1
            return A, B, G, sc
        else:
            sc = A[a]
            if A[a] + 1 > B[b] and a == b:
                A = np.delete(A, a)
                B = np.delete(B, b)
            else:
                A[a] += 1
            return A, B, G, sc


for T in range(int(input())):
    N, M = list(map(int, input().split()))
    A = np.empty(N)
    B = np.empty(N)
    for _ in range(N):
        A[_], B[_] = list(map(int, input().split()))
    S = list(map(int, input().split()))

    C = []
    G = []

    # print("A=", A)
    # print("B=", B)

    for s in S:
        A, B, G, c = getClosest(A, B, G, s)
        C.append(int(c))
    # print("A=", A, "B=", B)

    sp = ' '
    print(f"Case #{T+1}: {sp.join(map(str, C))}")
