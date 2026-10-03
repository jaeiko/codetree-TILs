#include <iostream>
#include <algorithm>
#define MAX_N 205

using namespace std;

int n, m;
int grid[MAX_N][MAX_N];
int max_sum = 0;

// 격자 범위 검사 함수
bool InRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

// 직교하는 인접 방향 (남, 서, 북, 동)
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, -1, 0, 1};

int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }
    }

    // 1. ㄱ자 블록 탐색: 꺾이는 꼭짓점을 (x, y)로 두고 직교하는 두 방향 확인
    for (int x = 0; x < n; x++) {
        for (int y = 0; y < m; y++) {
            for (int dir = 0; dir < 4; dir++) {
                int nx1 = x + dx[dir];
                int ny1 = y + dy[dir];
                int nx2 = x + dx[(dir + 1) % 4];
                int ny2 = y + dy[(dir + 1) % 4];

                // 둘 중 하나라도 범위를 벗어나면 유효하지 않은 블록

                if (!InRange(nx1, ny1) || !InRange(nx2, ny2)) continue;

                int current_sum = grid[x][y] + grid[nx1][ny1] + grid[nx2][ny2];

                max_sum = max(max_sum, current_sum);
            }
        }
    }

    // 2. 일자 블록 탐색: 가로(1x3) 및 세로(3x1)
    for (int x = 0; x < n; x++) {
        for (int y = 0; y < m; y++) {
            // 가로 3칸
            if (InRange(x, y + 2)) {
                int current_sum = grid[x][y] + grid[x][y + 1] + grid[x][y + 2];
                max_sum = max(max_sum, current_sum);
            }

            // 세로 3칸
            if (InRange(x + 2, y)) {
                int current_sum = grid[x][y] + grid[x+1][y] + grid[x+2][y];
                max_sum = max(max_sum, current_sum);
            }
        }
    }

    cout << max_sum << "\n";

    return 0;
}