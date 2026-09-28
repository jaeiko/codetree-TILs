#include <iostream>
#include <vector>
#include <utility>

using namespace std;
const int MAX_N = 105;

int n, m, t;
int grid[MAX_N][MAX_N];
int marble_count[MAX_N][MAX_N]; // 현재 각 좌표당 구슬 개수
int next_count[MAX_N][MAX_N];   // 다음 각 좌표당 구슬 개수

// 상, 하, 좌, 우
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

bool InRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < n;
}

// (x, y) 에 있는 구슬이 이동할 다음 좌표를 찾아 반환
pair<int, int> GetNextPos(int x, int y) {
    int max_val = 0;
    pair<int, int> best_pos = {x, y};

    // 상, 하, 좌, 우 순서대로 탐색
    for (int dir = 0; dir < 4; dir++) {
        int nx = x + dx[dir];
        int ny = y + dy[dir];

        if (!InRange(nx, ny)) continue;

        // 더 큰 값을 만났을 때만 갱신(동률일 경우 앞선 방향이 유지)
        if (grid[nx][ny] > max_val) {
            max_val = grid[nx][ny];
            best_pos = {nx, ny};
        }
    }

    return best_pos;
}

// 1초 동안의 모든 구슬의 동시 이동 및 충돌 처리
void Simulate() {
    // 1. next_count 초기화
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            next_count[i][j] = 0;
        }
    }

    // 2. 모든 구슬을 동시에 다음 위치로 이동
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if(marble_count[i][j] == 1) {
                pair<int, int> next_pos = GetNextPos(i, j);
                next_count[next_pos.first][next_pos.second]++;
            }
        }
    }

    // 3. 충돌 처리: 2개 이상의 구슬이 모인 칸은 전부 소멸 (0으로 초기화)
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (next_count[i][j] >= 2) {
                next_count[i][j] = 0;
            }
        }
    }

    // 4. next_count -> marble_count
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            marble_count[i][j] = next_count[i][j];
        }
    }
}

int main() {
    cin >> n >> m >> t;

    // 격자 숫자 입력
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    // 구슬 초기 위치 입력 (1-based -> 0-based 변환)
    for (int i = 0; i < m; i++) {
        int r, c;
        cin >> r >> c;
        marble_count[r-1][c-1] = 1;
    }

    // T초 동안 시뮬레이션 반복
    while (t--) {
        Simulate();
    }

    // 남아있는 구슬 개수 합산
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            ans += marble_count[i][j];
        }
    }

    cout << ans << endl;
}