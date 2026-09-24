#include <iostream>

using namespace std;

int n;
int grid[100][100];
int cnt = 0;

// 북(-1, 0), 동(0, 1), 남(1, 0), 서(0, -1)
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

bool InRange(int x, int y, int n) {
    return (0 <= x && x < n && 0 <= y && y < n);
}

int main() {
    cin >> n;

    // 격자 입력
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    // Please write your code here.
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int near_cnt = 0;
            for (int dir_num = 0; dir_num < 4; dir_num++) {
                int nx = i + dx[dir_num], ny = j + dy[dir_num];
                if (InRange(nx, ny, n) && grid[nx][ny] == 1) near_cnt++;
            }
            if (near_cnt >= 3) cnt++;
        }
    }

    cout << cnt << endl;

    return 0;
}