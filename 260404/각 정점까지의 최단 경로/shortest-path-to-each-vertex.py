import heapq
import sys

# 빠른 입력을 위한 설정
input = sys.stdin.readline
INT_MAX = sys.maxsize

# 1. N(정점), M(간선) 입력
n, m = map(int, input().split())

# 2. 시작 정점 K 입력
k = int(input())

# 3. 그래프 초기화 및 간선 정보 입력 (무방향)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    # 무방향 그래프이므로 양쪽 방향 모두 추가
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(start_node):
    # 거리 배열 초기화
    dist = [INT_MAX] * (n + 1)
    dist[start_node] = 0
    
    pq = []
    # (거리, 정점) 형태로 큐에 삽입
    heapq.heappush(pq, (0, start_node))
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        # 이미 처리된 노드라면 스킵 (!= 대신 > 사용도 가능)
        if current_dist > dist[current_node]:
            continue
            
        for neighbor, weight in graph[current_node]:
            new_cost = current_dist + weight
            
            # 더 짧은 경로를 발견한 경우 갱신
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
                
    return dist

# 4. 알고리즘 실행
result_distances = dijkstra(k)

# 5. 결과 출력 (1번부터 N번 정점까지)
for i in range(1, n + 1):
    if result_distances[i] == INT_MAX:
        print(-1) # 도달할 수 없는 경우
    else:
        print(result_distances[i])