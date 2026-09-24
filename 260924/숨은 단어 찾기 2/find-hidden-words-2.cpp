#include <iostream>
#include <string>

#define DIR_NUM 8

using namespace std;

int N, M;   // N * M 크기
string arr[55]; // 크기가 0인 빈 문자열 50개가 생성
int cnt = 0;

bool InRange(int x, int y, int n, int m) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

//남동, 남, 남서, 서, 북서, 북, 북동, 동
int dx[DIR_NUM] = {1, 1, 1, 0, -1, -1, -1, 0};
int dy[DIR_NUM] = {1, 0, -1, -1, -1, 0, 1, 1};

int x = 0, y = 0;

int main() {
    cin >> N >> M;
    for (int i = 0; i < N; i++)
        cin >> arr[i];  // string arr로 선언된 경우 이렇게 작성하는 걸 잊지말자. (만약 2중반복문 사용하여 cin >> arr[i][j] 사용할 거면 char arr[50][50] 이런식으로 선언했어야 했다.)


    // Please write your code here.
    for (int x = 0; x < N; x++) {
        for (int y = 0; y < M; y++){
            for (int dir = 0; dir < DIR_NUM; dir++) {
                int nx = x + dx[dir];
                int ny = y + dy[dir];

                // L로 시작하지 않거나 범위 벗어나면 패스
                if (arr[x][y] != 'L' || !InRange(nx, ny, N, M)) continue;
                // L로 시작하면 나머지 E 2개 체크
                int x2 = nx;
                int y2 = ny;
                
                nx = x2 + dx[dir];
                ny = y2 + dy[dir];
                if (arr[x2][y2] != 'E' || !InRange(nx, ny, N, M)) continue;
                else if (arr[nx][ny] == 'E') cnt += 1;
            }
        }
    }

    cout << cnt << endl;

    return 0;
}