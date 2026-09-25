#include <iostream>
#include <vector>

using namespace std;

int n;
int grid[200][200];
int r, c;
int x, y;   // r, c를 알아보기 쉽게 x, y로
int nx, ny;

int dx[4] = {1, 0, 0, -1};
int dy[4] = {0, 1, -1, 0};

bool InRange(int x, int y, int n) {
    return 0 <= x && x < n && 0 <= y && y < n;
}

int main() {
    cin >> n;

    // 2차원 n*n 배열 만드는 방법 잊지말기!
    vector<vector<int>> grid(n, vector<int>(n, 0));
    vector<vector<int>> temp(n, vector<int>(n, 0));

    // 그리드 입력
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    // // 디버깅용(grid 체크)
    // for (int i = 0; i < n; i++ ){
    //     for (int j = 0; j < n; j++) {
    //         cout << grid[i][j] << ' ';
    //     }
    //     cout << endl;
    // }

    cin >> r >> c;  // r행 c열이 폭탄(1 <= r, 1 <= c)
    x = r - 1;
    y = c - 1;

    // Please write your code here.
    // 폭탄 반경 범위 애들을 다 0으로 만듦.

    int bomb_range = grid[x][y];

    if (n != 1) {
        for (int i = 0; i < bomb_range; i++) {
            for (int dir_num = 0; dir_num < 4; dir_num++) {
                nx = x + dx[dir_num] * i;
                ny = y + dy[dir_num] * i;

                if (!InRange(nx, ny, n)) continue;

                // 오답노트: i = 0일 때 grid[x][y] = 0이 되니 반복문에서 1<0이 될 수 있으므로 i < grid[x][y] 대신 i < bomb_range를 사용하자!!
                grid[nx][ny] = 0;
            }
        }
    }
    // 마지막 자기 자신도 0으로 만듦.(n = 1일 때)
    grid[x][y] = 0;

    // // 디버깅용(폭발 후 grid 체크)
    // for (int i = 0; i < n; i++ ){
    //     for (int j = 0; j < n; j++) {
    //         cout << grid[i][j] << ' ';
    //     }
    //     cout << endl;
    // }

    int temp_x;
    int temp_y;
    // 남아있는 애들을 temp에 쌓기 (이때 머리 잘 굴리면서 i, j 위치 잘 따지기!!)
    for (int i = n-1; i >= 0; i--) {
        temp_x = n-1;
        temp_y = i;
        for (int j = n-1; j >= 0; j--) {
            if (grid[j][i] != 0){
                temp[temp_x][temp_y] = grid[j][i];
                temp_x -= 1;
            }
        }
    }

    // 출력
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << temp[i][j] << ' ';
        }
        cout << endl;
    }

    return 0;
}
