"""
Google Kick Start - Round B 2021 - Q1 [SOLVED]
Daniel Cortild - 19/04/2021
"""

for T in range(int(input())):
    N = int(input())
    S = input()
    A = [1]

    for i in range(1, len(S)):
        if S[i] > S[i - 1]:
            A.append(A[i - 1] + 1)
        else:
            A.append(1)

    spc = ' '
    print(f"Case #{T+1}: {spc.join(map(str, A))}")
