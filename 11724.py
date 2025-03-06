import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

#노드, 간선의 갯수
n,m = map(int, input().split())
# 인접리스트 생성 (index를 1부터 쓸거라 노드개수 +1개)
A = [[] for _ in range(n+1)]
#방문리스트 생성
visited = [False]*(n+1)

# 인접리스트 입력 
for i in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s) #방향이 없는 그래프라 양방향에 삽입
    

#DFS 
def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

result = 0

for i in range(1,n+1):
    if not visited[i]:
        DFS(i)
        result +=1

print(result)