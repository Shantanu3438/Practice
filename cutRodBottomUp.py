r = [-1, -1, -1, -1, -1]
p = [0, 1, 5, 8, 9]
def cutRod(p, n):
    r[0] = 0
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]
print(cutRod(p, 4))
print(r)
