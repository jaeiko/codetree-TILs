import heapq
import sys

# 빠른 입력을 위한 설정
input = sys.stdin.readline

INT_MAX = sys.maxsize

# N(정점), M(간선) 입력
n, m = map(int, input().split())

# Please write your code here.
# 그래프 초기화(인접리스트) 및 간선 정보 입력(방향)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    
    i, j, d = map(int, input().split())
    # 이때 간선을 뒤집어 넣는 것이 포인트이다.
    graph[j].append((d, i))

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
                heapq.heappush(pq, (new_cost, neighbor))
    
    return dist

# dijkstra 알고리즘 실행
# n번 학교를 시작점으로 하여 탐색을 시작해서 모든 정점까지의 거리를 구한다.
result_distances = dijkstra(n)

# 중요: 0번 인덱스를 제외(1부터 시작)하고, INT_MAX가 아닌 유효한 거리만 필터링(0번 거리는 무한대로 초기화했으니 걸려야 한다)
valid_distances = [d for d in result_distances[1:] if d != INT_MAX]

# 유효한 거리 중 최댓값을 출력
print(max(valid_distances))