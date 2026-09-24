#include <iostream>
#include <string>   // string 길이 length() 사용

using namespace std;

string dirs;

// 북, 동, 남, 서
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1 , 0};

int nx = 0;
int ny = 0;

int dir_num = 0; // 북쪽을 바라보고 있는 상태에서 시작

int main() {
    cin >> dirs;

    // Please write your code here.
    for (int i = 0; i < dirs.length(); i++) {
        if (dirs[i] == 'F') {
            nx += dx[dir_num];
            ny += dy[dir_num];
        } else if (dirs[i] == 'L') {
            dir_num = (dir_num + 3) % 4;
        } else if (dirs[i] == 'R') {
            dir_num = (dir_num + 1) % 4;
        }
    }

    cout << nx << ' ' << ny << endl;

    return 0;
}