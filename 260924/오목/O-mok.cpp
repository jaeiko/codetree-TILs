#include <iostream>
#include <algorithm>

#define DIR_NUM 8

using namespace std;

int arr[19][19];    // 바둑판

// key point : dx, dy 테크닉
int dx[DIR_NUM] = {1, 1, 1, -1, -1, -1, 0, 0};
int dy[DIR_NUM] = {-1, 0, 1, -1, 0, 1, -1, 1};

int InRange(int x, int y) {
    return 0 <= x && x < 19 && 0 <= y && y < 19;
}

int main() {
    // 입력 받기
    for (int i = 0; i < 19; i++)
        for (int j = 0; j < 19; j++)
            cin >> arr[i][j];

    // 모든 좌표에서 다 확인
    for (int i = 0; i < 19; i++)
        for (int j = 0; j < 19; j++) {
            // 해당 바둑좌표 위에 아무것도 안놓여져 있으면 패스
            if (arr[i][j] == 0) continue;

            for (int k = 0; k < DIR_NUM; k++) {
                int curt = 1;   // 5개 연속이지 체크하는 변수
                int curx = i;
                int cury = j;

                while(true) {
                    int nx = curx + dx[k];
                    int ny = cury + dy[k];

                    if(InRange(nx, ny) == false) break;

                    if(arr[nx][ny] != arr[i][j]) break;

                    curt++;
                    curx = nx;
                    cury = ny;
                }
                if (curt == 5) {
                    cout << arr[i][j] << endl;
                    cout << i +2 * dx[k] + 1 << " " << j + 2 * dy[k] + 1 << endl;

                    return 0;
                }
            }
        }

        // 아무것도 이긴 경우가 없으면 0 출력
        cout << 0 << '\n';

        return 0;
}