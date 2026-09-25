#include <iostream>
#include <climits>

using namespace std;

int n, m;
int grid[200][200] = {0};

// 최종 값
int max_sum = INT_MIN;

// 중간 계산값
int mid_cal = 0;

// 기준점
int x = 0, y = 0;

// 범위 체크
bool InRange(int x, int y, int n, int m) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

// dx, dy: 남, 서, 북, 동
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, -1, 0, 1};

int main() {
    cin >> n >> m;

    // 입력
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }
    }

    // Please write your code here.

    // 0이거나 범위 밖이면 좌표 옮기거나 다음 방향으로
    // case1: ㄱ자 모양
    for (int x = 0; x < n; x++) {
        // cout << "==== ㄱ자 모양 ====" << endl;
        for (int y = 0; y < m; y++) {
            for (int dir_num=0; dir_num < 4; dir_num++) {
                // 만약 현재 위치가 범위 밖이면 패스
                if (grid[x][y] == 0) continue;

                int nx = x + dx[dir_num];
                int ny = y + dy[dir_num];
                int nx2= x + dx[(dir_num + 1) % 4];
                int ny2= y + dy[(dir_num + 1) % 4];

                // 만약 nx, ny, nx2, ny2가 범위 밖이면 패스
                if (!InRange(nx, ny, n, m) || !InRange(nx2, ny2, n, m)) continue;
                mid_cal += grid[x][y] + grid[nx][ny] + grid[nx2][ny2];

                if (mid_cal > max_sum) {
                    max_sum = mid_cal;
                    // cout << "grid: " << grid[x][y] << ' ' << grid[nx][ny] << ' ' << grid[nx2][ny2] << endl;
                    // cout << "x: " << x << " y: " << y << " nx : " << nx << " ny: " << ny << " nx2: " << nx2 << " ny2: " << ny2 << endl;
                }
                mid_cal = 0;

            }
        }
    }

    // case2: 막대 모양
    for (int x = 0; x < n; x++) {
        // cout << "==== 막대 모양 ====" << endl;
        for (int y = 0; y < m; y++) {
            for (int dir_num=0; dir_num < 4; dir_num++) {
                // 만약 현재 위치가 범위 밖이면 패스
                if (grid[x][y] == 0) continue;

                int nx = x + dx[dir_num];
                int ny = y + dy[dir_num];
                int nx2= x + dx[dir_num] * 2;
                int ny2= y + dy[dir_num] * 2;

                // 만약 nx, ny, nx2, ny2가 범위 밖이면 패스
                if (!InRange(nx, ny, n, m) || !InRange(nx2, ny2, n, m)) continue;
                
                mid_cal += grid[x][y] + grid[nx][ny] + grid[nx2][ny2];

                if (mid_cal > max_sum) {
                    max_sum = mid_cal;
                    // cout << "grid: " << grid[x][y] << ' ' << grid[nx][ny] << ' ' << grid[nx2][ny2] << endl;
                }
                mid_cal = 0;
            }
        }
    }
    
    cout << max_sum << endl;
    return 0;
}
