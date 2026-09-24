#include <iostream>

using namespace std;

int n;
char dir[100];
int dist[100];

// 동, 남, 서, 북
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, -1, 0, 1};

int nx = 0;
int ny = 0;

int dir_num = 0;

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> dir[i] >> dist[i];
        if (dir[i] == 'N') dir_num = 3;
        else if (dir[i] == 'E') dir_num = 0;
        else if (dir[i] == 'S') dir_num = 1;
        else if (dir[i] == 'W') dir_num = 2;

        nx += dx[dir_num] * dist[i];
        ny += dy[dir_num] * dist[i];
    }

    // Please write your code here.

    cout << nx << ' ' << ny << endl;


    return 0;
}