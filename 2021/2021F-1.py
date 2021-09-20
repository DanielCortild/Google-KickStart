"""
Google Kick Start - Round F 2021 - Q1 [SOLVED]
Daniel Cortild - 18/09/2021
"""


def midDistance(n):
    sum = 0
    for i in range(n):
        sum += min(i+1, n-i)
    return sum

def endDistance(n):
    return n*(n+1)//2


for T in range(int(input())):
    N = int(input())
    S = input()

    first = False
    L = 0
    total = 0

    for c in S:
        if c == '1':
            if not first:
                first = True
                total += endDistance(L)
            else:
                total += midDistance(L)
            L = 0
        else:
            L += 1

    total += endDistance(L)

    print(f"Case #{T+1}: {total}")
