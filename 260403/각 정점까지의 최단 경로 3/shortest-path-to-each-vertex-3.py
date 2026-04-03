import sys
import heapq

# 1. 입력 받기
# n: 정점의 개수, m: 간선의 개수
input = sys.stdin.readline # 빠른 입력을 위해 추천
n, m = map(int, input().split())

# 2. 그래프(인접 리스트) 초기화 (1번 노드부터 시작한다고 가정하여 n+1)
graph = [[] for _ in range(n + 1)]

# 3. 간선 정보 입력
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w)) # u번에서 v번으로 가는 가중치 w

def dijkstra(start):
    # 최단 거리 테이블을 무한대로 초기화
    distances = [sys.maxsize] * (n + 1)
    distances[start] = 0
    
    # 우선순위 큐를 위한 빈 리스트 생성 및 시작점 삽입
    queue = []
    heapq.heappush(queue, (0, start)) # (거리, 노드) 튜플 형태로 우선순위 큐에 삽입
    
    while queue:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        current_distance, current_node = heapq.heappop(queue)
        
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시(해당 거리가 기존 거리보다 크다면 이미 그 노드는 처리한 것)
        if distances[current_node] < current_distance:
            continue
            
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for adjacent_node, weight in graph[current_node]:
            cost = current_distance + weight
            
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distances[adjacent_node]:
                distances[adjacent_node] = cost
                heapq.heappush(queue, (cost, adjacent_node))
                
    return distances

# 4. 알고리즘 실행
result = dijkstra(1) # 1번 노드에서 시작

# 결과 출력
for i in range(2, n + 1):   # i=1일 떄는 시작노드(거리 0)이므로 i=2부터 출력
    if result[i] == sys.maxsize:    # 해당 노드는 도달 불가
        print(-1)
    else:
        print(result[i])