#include <iostream>
#include <queue>
#include <utility>

using namespace std;

const int MAX_N = 105;

int n, k;
int grid[MAX_N][MAX_N];
bool visited[MAX_N][MAX_N];
queue<pair<int, int>> q;
int cnt = 0;

// 상, 하, 좌, 우
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

bool InRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < n;
}

// 갈 수 있는 칸인지 검사(0:이동 가능, 1: 벽)
bool CanGo(int x, int y) {
    if(!InRange(x, y)) return false;
    if(visited[x][y] || grid[x][y] == 1) return false;
    return true;
}

// 큐 삽입, 방문 표시, 카운트를 한 번에 수행
void Push(int x, int y) {
    visited[x][y] = true;
    q.push({x, y});
    cnt++;
}

void BFS() {
    while (!q.empty()) {
        pair<int, int> curr_pos = q.front();
        q.pop();

        int x = curr_pos.first;
        int y = curr_pos.second;

        for (int i = 0; i < 4; i++) {
            int new_x = x + dx[i];
            int new_y = y + dy[i];

            // 안전 검사를 통과한 경우에만 Push 수행
            if (CanGo(new_x, new_y)) {
                Push(new_x, new_y);
            }
        }
    }
}

int main() {
    cin >> n >> k;

    // 격자 입력 (0: 갈 수 있는 곳, 1: 벽)
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    // k개의 시작점 입력 및 다중 시작점 큐 초기화
    for (int i = 0; i < k; i++) {
        int r, c;
        cin >> r >> c;
        int start_x = r-1;
        int start_y = c-1;

        // 시작 칸이 벽이 아니고 아직 방문하지 않은 경우 큐에 삽입
        Push(start_x, start_y);
    }

    BFS();
    cout << cnt << endl;

    return 0;
}