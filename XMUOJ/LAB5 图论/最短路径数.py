"""
4 5
2 4
1 2
2 3
1 3
3 4
"""


N,E = map(int,input().split())
G = [[] for _ in range(N+1)]

for _ in range(E):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

from collections import deque

min_dist = 0
path_counter = 0

q = deque([(1, set(), 0)])
while(q):
    u,visited,dist = q.popleft()
    visited.add(u)
    # print(u)
    if u == N or dist >= min_dist: 
        min_dist = dist
        path_counter = (path_counter+1)%(10**9+7)
        continue
    for v in G[u]:
        if v not in visited:
            q.append((v,visited,dist+1))

print(path_counter)