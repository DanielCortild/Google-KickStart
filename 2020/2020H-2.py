"""
Google Kick Start - Round H 2020 - Q2 [NOT SOLVED ~> BROKEN]
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

def interestingLessThanR(R):
	print("INTERESTING LESS THAN", R)
	if R == 0: return 0
	if R < 10: return R // 2 + 1
	if R == 10: return 5
	nb = 5 ** (math.floor(math.log10(R)))
	r = R // 10 ** math.floor(math.log10(R))
	R2 = R - r * 10 ** math.floor(math.log10(R))
	if r > 1:
		print(r // 2 + 1, "times boring less than ", 10 ** math.floor(math.log10(R)) - 1)
		to_add = boringLessThanR(10 ** math.floor(math.log10(R)) - 1, True) * (r // 2 + 1) # BORING
		print(r // 2 + 1, "times boring less than ", 10 ** math.floor(math.log10(R)) - 1, "=>", to_add)
		nb += to_add
	if not r % 2:
		nb += boringLessThanR(R2, True) # BORING
	return nb

def boringLessThanR(R, from_int=False):
	print("BORING LESS THAN", R)
	if R < 10: return (R + 1) // 2
	if R == 10: return 6
	if from_int:
		nb = 5 ** math.floor(math.log10(R)) 
	else:
		nb = (5 ** (math.floor(math.log10(R)) + 1) - 1) / 4 - 1
	r = R // (10 ** math.floor(math.log10(R)))
	R2 = R - r * 10 ** math.floor(math.log10(R))
	if r > 1:
		print((r - 1) // 2, "times interesing less than ", 10 ** math.floor(math.log10(R)) - 1)
		to_add = interestingLessThanR(10 ** math.floor(math.log10(R)) - 1) * ((r - 1) // 2)
		print((r - 1) // 2, "times interesing less than ", 10 ** math.floor(math.log10(R)) - 1, "=>", to_add)
		nb += to_add # INTERESTING
	if r % 2:
		nb += interestingLessThanR(R2)# INTERESTING
	return nb

def boringLTR(R):
	first = R // 10 ** math.floor(math.log10(R))
	nb = first // 2 * (5 ** math.floor(math.log10(R)))
	

# for T in range(int(input())):
# 	L, R = map(int, input().split())
# 	print("Case #{}: {}".format(T+1, int(boringLessThanR(R) - boringLessThanR(L-1))))

# print(boringLessThanR(9999))
print(interestingLessThanR(99))