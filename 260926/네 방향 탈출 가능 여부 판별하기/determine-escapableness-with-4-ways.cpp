#include <iostream>
#include <queue>
#include <utility>
#include <vector>
#define MAX_N = 105;

using namespace std;

int n, m;

vector<vector<int>> grid;
vector<vector<bool>> visited;
queue<pair<int, int>> q;

// 상, 하 , 좌, 우
int dx[4] = {-1, 1,0 ,0 };
int dy[4] = {0, 0, -1, 1};

// 격자 경계 검사 함수
bool InRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

// 갈 수 있는 칸인지 검사
bool CanGo(int x, int y) {
    // 격자 밖이면 이동 불가
    if(!InRange(x, y)) return false;
    if(visited[x][y] || grid[x][y] == 0) return false;

    return true;
}

void BFS() {


    while(!q.empty()) {
        pair<int, int> curr_pos = q.front();
        q.pop();

        int x = curr_pos.first;
        int y = curr_pos.second;

        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(CanGo(nx, ny)) {
                visited[nx][ny] = true;
                q.push({nx, ny});
            }
        }
    }
}

int main() {
    cin >> n >> m;
    
    grid.assign(n, vector<int>(m, 0));
    visited.assign(n, vector<bool>(m, false));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }
    }

    // Please write your code here.
if (grid[0][0] == 1) {
        visited[0][0] = true;
        q.push({0, 0});
        BFS();
    }

    if (visited[n-1][m-1]) {
        cout << 1 << endl;
    } else {
        cout << 0 << endl;
    }


    return 0;
}
