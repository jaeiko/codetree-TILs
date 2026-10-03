#include <iostream>
#include <vector>

using namespace std;

int n, m;
vector<vector <int>> grid;

int curr_x = 0;
int curr_y = 0;

int DIR_NUM = 0;

bool InRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

bool CanGo(int x, int y) {
    if (!InRange(x, y)) return false;
    if (grid[x][y] != 0) return false;
    return true;
}

// 동, 남, 서, 북
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int main() {
    cin >> n >> m;
    grid.assign(n, vector(m, 0));

    grid[0][0] = 1;

    int count = n * m - 1;

    // Please write your code here.
    while(count) {
        int new_x = curr_x + dx[DIR_NUM];
        int new_y = curr_y + dy[DIR_NUM];

        if (CanGo(new_x, new_y)) {
            grid[new_x][new_y] = grid[curr_x][curr_y] + 1;
            curr_x = new_x;
            curr_y = new_y;

            count -= 1;
        } else {
            DIR_NUM = (DIR_NUM + 1) % 4;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << grid[i][j] << ' ';
        }
        cout << endl;
    }

    return 0;
}