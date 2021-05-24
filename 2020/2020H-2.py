"""
Google Kick Start - Round H 2020 - Q1 [ONLY TEST 1]
Daniel Cortild - 15/11/2020
"""

import math

def isBoring(x):
	if x%100 == 0: return False
	if x%10 == 0 and math.floor(math.log(x, 10)+1) % 2 == 1: return False
	x = int(str(x)[::-1])
	boring = 0
	for i in range(math.ceil(math.log(x, 10))):
		l = x % 10
		boring += (l+i+1) % 2
		x -= l
		x /= 10

	return boring == 0


for T in range(int(input())):
    L, R = map(int, input().split())
    sol = 0
    for i in range(L, R+1):
        sol += isBoring(i)
    print("Case #{}: {}".format(T+1, sol))

