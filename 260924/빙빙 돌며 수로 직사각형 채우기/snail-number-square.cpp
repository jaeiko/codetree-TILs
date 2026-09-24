#include <iostream>
#include <vector>

using namespace std;

int n, m;   // n행 m열
int x = 0, y = 0;

// 동(0, 1), 남(1, 0), 서(0, -1), 북(-1, 0)
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int dir_num = 0;

// 범위 체크
bool InRange(int x, int y, int n, int m) {
    return (0 <= x && x < n && 0 <= y && y < m);
}

int main() {
    cin >> n >> m;
    // int arr[n][m] = {0}; -> 이렇게는 못쓴다. 유의하자.
    // 내가 방금 만든 m칸짜리 가로 줄(vector<int>(m,0))을 세로로 n층만큼 쌓아서 arr라는 이름의 2차원 배열을 만들어달라는 의미
    vector<vector<int>> arr(n, vector<int>(m, 0));

    arr[x][y] = 1;

    // Please write your code here.
    for (int i = 2; i <= n * m; i++){
        int nx = x + dx[dir_num];
        int ny = y + dy[dir_num];
        if (!InRange(nx, ny, n, m) || arr[nx][ny] != 0) {
            // 방향 바꿔야 하는 경우(범위 벗어나거나 값이 이미 존재)
            dir_num = (dir_num + 1) % 4;
        }          
        x = x + dx[dir_num];
        y = y + dy[dir_num];
        arr[x][y] = i;
    }

    // 결과 출력
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << arr[i][j] << ' ';
        }
        cout << endl;
    }


    return 0;
}