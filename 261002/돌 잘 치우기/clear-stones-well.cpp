#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>

using namespace std;

int n, k, m;
int grid[100][100];
bool visited[100][100];

// 이동 방향(상, 하, 좌, 우)
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

vector<pair<int, int>> stones;      // 격자 내 모든 돌의 위치
vector<pair<int, int>> selected_stones; // 치우기로 선택한 M개의 돌
vector<pair<int, int>> start_points;    // K개의 시작점 위치

int max_cnt = 0;

bool InRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < n;
}

bool CanGo(int x, int y) {
    if (!InRange(x, y)) return false;
    if (visited[x][y] || grid[x][y] == 1) return false;
    return true;
}

// K개의 시작점으로부터 이동 가능한 칸의 수를 세는 BFS
int BFS() {
    memset(visited, false, sizeof(visited));
    queue<pair<int, int>> q;
    int reachable_cnt = 0;

    // 모든 시작점을 큐에 먼저 넣고 방문 처리
    for (const auto& sp : start_points) {
        int sx = sp.first;
        int sy = sp.second;
        if (!visited[sx][sy]) {
            visited[sx][sy] = true;
            q.push({sx, sy});
            reachable_cnt++;
        }
    }

    while (!q.empty()) {
        int cx = q.front().first;
        int cy = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];

            if (CanGo(nx, ny)) {
                visited[nx][ny] = true;
                q.push({nx, ny});
                reachable_cnt++;
            }
        }
    }

    return reachable_cnt;
}

// 백트래킹을 통해 stones 중 M개를 선택하는 조합 생성
void FindMaxReachable(int idx, int count) {
    if (count == m) {
        // 1. 처음에 M개의 돌을 치움 (0으로 변경)
        for (const auto& stone : selected_stones) {
            grid[stone.first][stone.second] = 0;
        }

        // 2. BFS 탐색을 통해 도달 가능한 칸 수 계산 및 최댓값 갱신
        max_cnt = max(max_cnt, BFS());

        // 3. 원상 복구 (다시 1로 변경)
        for (const auto& stone : selected_stones) {
            grid[stone.first][stone.second] = 1;
        }
        return;
    }

    // 더 이상 탐색할 돌이 없는 경우
    if (idx >= (int)stones.size()) return;

    // 현재 idx번째 돌을 치우는 경우(왼쪽 가지라고 생각하면 됨)
    selected_stones.push_back(stones[idx]);
    FindMaxReachable(idx + 1, count + 1);
    selected_stones.pop_back();

    // 현재 idx 번째 돌을 치우지 않는 경우(오른쪽 가지라고 생각하면 됨)
    FindMaxReachable(idx + 1, count);
}

int main() {
    cin >> n >> k >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
            if (grid[i][j] == 1) {
                stones.push_back({i, j});
            }
        }
    }

    for (int i = 0; i < k; i++) {
        int r, c;
        cin >> r >> c;
        start_points.push_back({r - 1, c - 1});
    }

    FindMaxReachable(0, 0);

    cout << max_cnt << endl;

    return 0;
}