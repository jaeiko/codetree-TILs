#include <iostream>

using namespace std;

int n;
int curr_x, curr_y;
int a[101][101];

// 상 하 좌 우
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

bool InRange(int x, int y) {
    return 1 <= x && x <= n && 1 <= y && y <= n;
}

// 1회 이동을 시도하고 이동 여부를 반환하는 함수
bool Simulate() {
    // 상, 하, 좌, 우 순서대로 탐색
    for (int i = 0; i < 4; i++) {
        int next_x = curr_x + dx[i];
        int next_y = curr_y + dy[i];

        // 격자 내에 있고, 현재 칸보다 숫자가 크다면 즉시 이동(우선순위 최고)
        if (InRange(next_x, next_y) && a[next_x][next_y] > a[curr_x][curr_y]) {
            curr_x = next_x;
            curr_y = next_y;
            cout << a[curr_x][curr_y] << " ";
            return true;    // 이동 성공
        }
    }
    return false;
}

// 4방향 모두 더 큰 숫자가 없다면 이동 불가

int main() {
    cin >> n >> curr_x >> curr_y;

    // 입력
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> a[i][j];
        }
    }

    // Please write your code here.
    cout << a[curr_x][curr_y] << ' ';

    // 더 이상 이동할 수 없을 때까지 반복
    while(true) {
        if(!Simulate()) break;  // 종료 조건
    }

    return 0;
}