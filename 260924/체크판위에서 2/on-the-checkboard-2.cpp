#include <iostream>
#include <vector>

using namespace std;

int R, C;   // R X C 크기

int main() {
    int cnt = 0;

    cin >> R >> C;

    // 벡터 초기화 방식 익히기
    vector<vector<char>> grid(R, vector<char>(C, ' '));

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> grid[i][j];
        }
    }

    char start = grid[0][0];
    char finish = grid[R-1][C-1];

    // 다른 색깔로 넘어갈 때 무조건 현재 위치보다 아래, 오른쪽 위치로 가야한다.
    for (int i = 1; i < R; i++) {
        for (int j = 1; j < C; j++) {
            for (int k = i+1; k < R-1; k++) {
                for (int l = j+1; l < C-1; l++) {
                    if (grid[i][j] != grid[k][l] && start != grid[i][j] && finish != grid[k][l]) {
                        cnt += 1;
                    }
                }
            }
        }
    }

    // Please write your code here.
    cout << cnt << endl;

    return 0;
}