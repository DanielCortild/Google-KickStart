"""
Google Kick Start - Round F 2021 - Q2 [TEST 1]
Daniel Cortild - 18/09/2021
"""

def kLargest(arr, K):
    return sum(sorted(arr)[-K:])    

for T in range(int(input())):
    D, N, K = list(map(int, input().split()))
    possibilities = {}
    for i in range(D):
        possibilities[i] = []
    maxHappy = [0] * D

    for i in range(N):
        h, s, e = list(map(int, input().split()))
        for j in range(s-1, e):
            possibilities[j].append(h)
            possibilities[j] = sorted(possibilities[j])[-K:]

    for i in range(D):
        maxHappy[i] = sum(possibilities[i])

    print(f"Case #{T+1}: {max(maxHappy)}")
