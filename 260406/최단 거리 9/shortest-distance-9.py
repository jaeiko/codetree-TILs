import heapq
import sys

# 빠른 입력을 위한 설정
input = sys.stdin.readline

INT_MAX = sys.maxsize

# N(정점), M(간선) 입력
n, m = map(int, input().split())

# Please write your code here.
# 그래프 초기화(인접리스트) 및 간선 정보 입력(양방향)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, weight = map(int, input().split())
    graph[a].append((weight, b))
    graph[b].append((weight, a))

# path: 경로 배열
path = [0 for _ in range(n+1)]

def dijkstra(start_node):
    # 거리 배열 초기화
    dist = [INT_MAX] * (n + 1)
    dist[start_node] = 0
    pq = []

    heapq.heappush(pq, (0, start_node))

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # 이미 처리된 노드라면 스킵
        if current_dist > dist[current_node]:
            continue

        for weight, neighbor in graph[current_node]:
            new_cost = current_dist + weight

            # 더 짧은 경로를 발견한 경우 갱신
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                # path 갱신
                path[neighbor] = current_node
                heapq.heappush(pq, (new_cost, neighbor))

    return dist

# A, B: 정점 A, B
a, b = map(int, input().split())
# dijkstra 알고리즘 실행(a부터 시작)
result_distances = dijkstra(a)

# 경로 역추적 시작
x = b
vertices = []
vertices.append(x)

# 현재 노드가 시작점 a가 될 때까지 반복
while x != a:
    x = path[x]
    vertices.append(x)

print(result_distances[b])

# 거쳐간 순서를 거꾸로 출력한다.
for num in vertices[::-1]:
    print(num, end=" ")