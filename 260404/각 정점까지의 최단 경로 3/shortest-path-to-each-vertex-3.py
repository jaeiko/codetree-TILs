import sys
INT_MAX = sys.maxsize

n, m = map(int, input().split())

# Please write your code here.
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

# 그래프에 있는 모든 노드들에 대해 초기값을 전부 아주 큰 값으로 설정
dist = [INT_MAX] * (n + 1) 


#그래프를 인접행렬로 표현
for i in range(1, m+1):
    x, y, z = tuple(map(int, input().split()))
    graph[x][y] = z

#시작 위치 1번, 시작위치의 dist값을 0으로 설정
dist[1] = 0

# O(|V|^2) 다익스트라 코드
for i in range(1, n+1):
    # V개의 정점 중 아직 방문하지 않은 정점 중 dist값이 가장 작은 정점을 찾는다.
    min_index = -1
    for j in range(1, n+1):
        if visited[j]:
            continue
    
        if min_index == -1 or dist[min_index] > dist[j]:
            min_index = j

    # 최솟값에 해당하는 정점에 방문 표시
    visited[min_index] = True

    # 최솟값에 해당하는 정점에 연결된 간선들을 보며 시작점으로부터의 최단거리 값을 갱신
    for j in range(1, n+1):
        # 간선이 존재하지 않는 경우는 패스
        if graph[min_index][j] == 0:
            continue

        dist[j] = min(dist[j], dist[min_index] + graph[min_index][j])

# 시작점 이후부터 각 지점까지의 최단거리 값을 출력한다.
for i in range(2, n+1):
    if dist[i] == INT_MAX:
        print(-1)
    else:
        print(dist[i])