"""
Google Kick Start - Round D 2021 - Q4 [SOLVED]
Daniel Cortild - 11/07/2021
"""


class SegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.tree = [0] * (2 * self.n)
        self.build(array)

    def build(self, array):
        for i in range(self.n):
            self.tree[self.n + i] = array[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def query(self, left, right):
        res = 0
        left += self.n
        right += self.n
        while left < right:
            if (left & 1):
                res += self.tree[left]
                left += 1
            if (right & 1):
                right -= 1
                res += self.tree[right]
            left >>= 1
            right >>= 1
        return res

    def update(self, p, value):
        self.tree[p + self.n] = value
        p = p + self.n
        i = p
        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1


def V(a, P):
    if a == 0:
        return 0
    if a // P * P == a:
        return V(a // P, P) + 1
    return 0


for T in range(int(input())):
    N, Q, P = list(map(int, input().split()))
    V_AdivP = N * [0]
    V_AnotPn = N * [0]
    V_AnotPp = N * [0]
    V_AnotPC = N * [0]
    for i, a in enumerate(list(map(int, input().split()))):
        if a % P == 0:
            V_AdivP[i] = V(a, P)
        elif a > P:
            V_AnotPn[i] = V(a - (a % P), P)
            V_AnotPp[i] = V(a + 1, 2) - 1
            V_AnotPC[i] = 1
    ST_AdivP = SegmentTree(V_AdivP)
    ST_AnotPn = SegmentTree(V_AnotPn)
    ST_AnotPp = SegmentTree(V_AnotPp)
    ST_AnotPC = SegmentTree(V_AnotPC)
    C = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            p, v = query[1:]
            ST_AdivP.update(p - 1, V(v, P) if v % P == 0 else 0)
            ST_AnotPn.update(p - 1, V(v - (v % P), P)
                             if v % P != 0 and v > P else 0)
            ST_AnotPp.update(p - 1, V(v + 1, 2) - 1
                             if v % P != 0 and v > P else 0)
            ST_AnotPC.update(p - 1, 1 if v % P != 0 and v > P else 0)
        else:
            S, L, R = query[1:]
            c = ST_AdivP.query(L - 1, R) * S + \
                ST_AnotPC.query(L - 1, R) * V(S, P) + ST_AnotPn.query(L - 1, R)
            if P == 2 and S % 2 == 0:
                c += ST_AnotPp.query(L - 1, R)
            C.append(c)

    print(f"Case #{T+1}: {' '.join(map(str, C))}")
