import heapq
import sys

input = sys.stdin.readline

INT_MAX = sys.maxsize

# N: 정점 / M: 간선
n, m = map(int, input().split())

# Please write your code here.
# 그래프 인접리스트로 초기화
graph = [[] for _ in range(n+1)]

# 간선 정보 입력(양방향)
for _ in range(m):
    a, b, weight = map(int, input().split())
    graph[a].append((weight, b))
    graph[b].append((weight, a))

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
                heapq.heappush(pq, (new_cost, neighbor))

    return dist

# 경로를 구할 정점 A, B 입력
a, b = map(int, input().split())

# 도착점(b)를 시작으로 하는 역방향 다익스트라 실행
dist_from_b = dijkstra(b)

print(dist_from_b[a])

# 경로 역추적 시작(출발점 a부터)
# 뒤집힌 그래프를 기준으로 시작점 a에서 b까지 사전순 경로 탐색을 한다.
# 최단거리를 만족하는 경로 중 가장 간선 번호가 작은 곳으로 이동한다.
curr = a
path_result = [curr]
while curr != b:
    next_node = INT_MAX # 가장 작은 번호를 찾기 위해 무한대로 초기화

    for weight, neighbor in graph[curr]:
        # 시작점 -> neighbor -> ... -> 도착점(b)의 거리가 최단 거리와 일치하는지 체크
        if dist_from_b[curr] == weight + dist_from_b[neighbor]:
            # 조건을 만족하는 노드 중 가장 작은 번호만 갱신
            if neighbor < next_node:
                next_node = neighbor
            break;  # 번호가 가장 작은 조건을 만족했으므로 즉시 종료

    # 만약 길을 찾지 못했다면 종료(무한루프 방지)
    if next_node == INT_MAX:
        break
    
    curr = next_node
    path_result.append(curr)

# 결과 출력
for num in path_result:
    print(num, end=" ")