a = list(map(int, input().split()))

for i in range(0, len(a)-1):
    m = min(a[i:])
    ind = a.index(m)
    a[i], a[ind] = a[ind], a[i]

print(a)