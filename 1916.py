import sys
from queue import PriorityQueue
input = sys.stdin.readline

N = int(input())
M = int(input())
myList = [[] for _ in range(N + 1)]
dist = [sys.maxsize] * (N + 1)
visit = [False] * (N + 1)

for _ in range(M): #입력 받음
    start, end, weight = map(int, input().split())
    myList[start].append((end, weight))

start_idnex, end_index = map(int, input().split())

def dijkstra(start, end):
    pq = PriorityQueue()
    pq.put((0, start))
    dist[start] = 0
    while pq.qsize() > 0:
        nowNode = pq.get()
        nowCity = nowNode[1]
        if not visit[nowCity]:
            visit[nowCity] = True
            for n in myList[nowCity]:
                if dist[n[0]] > dist[nowCity] + n[1]:
                    dist[n[0]] = dist[nowCity] + n[1]
                    pq.put((dist[n[0]], n[0]))
    return dist[end]

print(dijkstra(start_idnex, end_index))