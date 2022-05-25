#первые 2 числа - кол-во узлов и кол-во ребер. Затем по очереди вводим каждое ребро

inp = list(map(int, input().split()))
n, m = inp[0], inp[1]


def ToDict(n, m):
    ribs = list()
    while m > 0:
        ribs.append(list(map(int, input().split())))
        m -= 1
    ribsDict = dict()
    for i in range(n):
        currRibs = []
        for j in range(len(ribs)):
            if ribs[j][0] == i + 1:
                currRibs.append(ribs[j][1])
            elif ribs[j][1] == i + 1:
                currRibs.append(ribs[j][0])
        ribsDict[i + 1] = currRibs
    return ribsDict


ribsDict = ToDict(n, m)

Visited = [False] * (n + 1)


def DFS(start, verts):
    Visited[start] = True
    verts.append(start)
    for u in ribsDict[start]:
        if not Visited[u]:
            DFS(u, verts)
    return verts


comps = list()

for i in range(1, n + 1):
    if not Visited[i]:
        comps.append(DFS(i, list()))

print(len(comps))
for i in range(len(comps)):
    print(len(comps[i]))
    print(' '.join(list(map(str, sorted(comps[i])))))