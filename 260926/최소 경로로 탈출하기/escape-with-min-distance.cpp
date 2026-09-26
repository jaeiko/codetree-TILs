#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <tuple>

using namespace std;

int n, m;
int x = 0, y = 0;

vector<vector<int>> grid;
vector<vector<int>> visited;    // visited의 최단경로 크기 구할 예정
queue<tuple<int, int, int>> q;

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

bool InRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

bool CanGo(int x, int y) {
    if (!InRange(x, y)) return false;
    if (visited[x][y] || grid[x][y] == 0) return false;

    return true;
}

void BFS() {
    while (!q.empty()) {
        tuple<int, int, int> curr_pos = q.front();
        q.pop();

        int x = get<0>(curr_pos);
        int y = get<1>(curr_pos);
        int cnt = get<2>(curr_pos);

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(CanGo(nx, ny)) {
                visited[nx][ny] = cnt;
                if (nx == n - 1 && ny == m - 1) return;  // 결승점까지 도달했으면 종료
                //cout << "nx: " << nx << " ny: " << ny << endl;
                //cout << "visited[nx][ny]: " << visited[nx][ny] << endl;
                q.push({nx, ny, visited[nx][ny] + 1});
            }
        }
    }
}

int main() {
    cin >> n >> m;

    grid.assign(n, vector<int>(m, 0));
    visited.assign(n, vector<int>(m, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }
    }

    // Please write your code here.
    if (grid[0][0] == 1) {
        visited[0][0] = 1;
        q.push({x, y, visited[0][0]});
        BFS();
    }

    if (visited[n-1][m-1]) {
        cout << visited[n-1][m-1] << endl;
    } else {
        cout << -1 << endl;
    }

    return 0;
}
