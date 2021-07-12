"""
Google Kick Start - Round A 2021 - Q1 [SOLVED]
Daniel Cortild - 21/03/2021
"""

import math

def getGoodnessNb(S):
    n = 0
    for i in range(math.floor(len(S) / 2)):
        if S[i] != S[len(S) - i - 1]:
            n += 1
    return n


for T in range(int(input())):
    N, K = list(map(int, input().split()))
    S = input()

    G = getGoodnessNb(S)

    print(f"Case #{T+1}: {abs(K-G)}")
