#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

const int MAX_N = 15;

int n;
int grid[MAX_N][MAX_N];
bool visited[MAX_N];
int min_val = INT_MAX;

// depth: 방문한 도시 수 (출발점 포함)
// curr: 현재 위치한 도시 인덱스
// cost: 현재까지 누적된 이동 비용
void FindMinCost(int depth, int curr, int cost) {
    // 가지치기: 이미 현재 비용이 최솟값 이상이면 더 탐색할 가치가 없음.
    if (cost >= min_val) return;

    // 모든 n개의 도시를 전부 방문한 경우
    if (depth == n) {
        // 마지막 도시에서 다시 출발점으로 돌아갈 수 있는 길이 있는지 확인
        if (grid[curr][0] != 0) {
            min_val = min(min_val, cost + grid[curr][0]);
        }
        return;
    }

    // 다음 방문할 도시 탐색(0번은 출발점이므로 1~n-1 탐색)
    for (int next = 0; next < n; next++) {
        // 이미 방문했거나, 길이 없는 경우(0) 패스
        if (visited[next] || grid[curr][next] == 0) continue;

        visited[next] = true;
        // cost + grid[curr][next] 형태로 넘기기(Call by Value 이용하면 독립적으로 사용가능)
        FindMinCost(depth + 1, next, cost + grid[curr][next]);
        visited[next] = false;  // 방문 복구
    }
}

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    // 0번 정점에서 출발 (방문 처리)
    visited[0] = true;
    FindMinCost(1, 0, 0);

    cout << min_val << endl;

    return 0;
}