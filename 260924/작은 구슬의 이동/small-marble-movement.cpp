#include <iostream>

using namespace std;

int n, t;   // n: 격자 크기, t: 시간
int r, c;   // 초기 구슬 위치(r행 c열)
char d;     // 방향(U, D, R, L)

// 북(-1, 0), 동(0, 1), 남(1, 0), 서(0, -1)
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

bool InRange(int x, int y, int n) {
    return (1 <= x && x <= n && 1 <= y && y <= n);
}

int GetDir(char a) {
    if (a == 'R') {
        return 1;
    } else if (a == 'D') {
        return 2;
    } else if (a == 'U') {
        return 0;
    } else return 3;
}

int main() {
    cin >> n >> t;
    cin >> r >> c >> d;
    int dir_num = GetDir(d);

    // Please write your code here.
    for (int i = 1; i <= t; i++) {
        if (InRange(r + dx[dir_num], c + dy[dir_num], n)) {
            r = r + dx[dir_num];
            c = c + dy[dir_num];
            // cout << "좌표: " << r << ' ' << c << endl;
        } else {
            dir_num = (dir_num + 2) % 4;
            // cout << "방향: " << dir_num << endl;
        }
    }

    cout << r << ' ' << c << endl;

    return 0;
}