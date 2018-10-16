def triangles():
    l = []
    while True:
        yield l
        l = [1] + [l[k] + l[k+1] for k in range(len(l)-1)] + [1]

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
       
