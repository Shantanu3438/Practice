def cutRod(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = - 1
    for i in range(1, n + 1):
        pass
        q = max(q, p[i] + cutRod(p, n - i, r))
        r[n] = q
    return q

r= [-1, -1, -1, -1, -1, -1, -1]
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(cutRod(p, 4, r))
for i in range(1, 6):
    print(r[i])
