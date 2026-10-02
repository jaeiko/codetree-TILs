#include <iostream>
#include <tuple>
#include <queue>
#include <utility>

#define MAX_N 100
#define DIR_NUM 4
#define NOT_EXISTS make_pair(-1, 1)

using namespace std;

int n, k;

int grid[MAX_N][MAX_N];

// 현재 위치
pair<int, int> curr_cell;

queue<pair<int, int>> bfs_q;
bool visited[MAX_N][MAX_N];

bool InRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < n;
}

bool CanGo(int x, int y, int target_num) {
    return InRange(x, y) && !visited[x][y] && grid[x][y] < target_num;
}

// visited 배열 초기화
void InitializeVisited() {
    for(int i = 0; i < n; i++) 
        for(int j = 0; j < n; j++)
            visited[i][j] = false;
}

void BFS() {
    int dx[DIR_NUM] = {0, 1, 0, -1};
    int dy[DIR_NUM] = {1, 0, -1, 0};

    int curr_x, curr_y;
    tie(curr_x, curr_y) = curr_cell;
    visited[curr_x][curr_y] = true;
    bfs_q.push(curr_cell);

    int target_num = grid[curr_x][curr_y];

    // BFS 탐색 수행
    while(!bfs_q.empty()) {
        pair<int, int> curr_pos = bfs_q.front();
        int curr_x, curr_y;
        tie(curr_x, curr_y) = curr_pos;
        bfs_q.pop();

        for (int i = 0; i < DIR_NUM; i++) {
            int new_x = curr_x + dx[i];
            int new_y = curr_y + dy[i];

            if(CanGo(new_x, new_y, target_num)) {
                bfs_q.push(make_pair(new_x, new_y));
                visited[new_x][new_y] = true;
            }
        }
    }
}

// best 위치를 새로운 위치로 바꿔줘야 하는지 판단해준다.
bool NeedUpdate(pair<int, int> best_pos, pair<int, int> new_pos) {
    // 첫 도달 가능한 위치라면 update가 필요하다.
    if(best_pos == NOT_EXISTS) return true;

    int best_x, best_y;
    tie(best_x, best_y) = best_pos;

    int new_x, new_y;
    tie(new_x, new_y) = new_pos;

    // 숫자, -행, -열 순으롣 더 큰 곳이 골라져야 한다.
    return make_tuple(grid[new_x][new_y], -new_x, -new_y) > make_tuple(grid[best_x][best_y], -best_x, -best_y);
}

// 가장 우선순위가 높은 위치를 찾아 위치를 이동한다.
bool Move() {
    // BFS 탐색을 위한 초기화 작업을 수행한다.
    InitializeVisited();

    // Step1. BFS를 진행하여 갈 수 있는 모든 위치를 탐색한다.
    BFS();

    // Step2. 도달 할 수 있는 위치들 중 가장 우선순위가 높은 위치를 구한다.
    pair<int, int> best_pos = NOT_EXISTS;
    for(int i = 0; i < n; i++) 
        for(int j = 0; j < n; j++) {
            // 도달이 불가능하거나 현재 위치는 건너뛴다.
            if(!visited[i][j] || make_pair(i, j) == curr_cell) continue;

            pair<int, int> new_pos = make_pair(i, j);
            if(NeedUpdate(best_pos, new_pos)) best_pos = new_pos;
        }

    // Step3. 위치를 이동한다.
    // 만약 움직일 위치가 없다면 종료한다.
    if (best_pos == NOT_EXISTS) return false;
    // 움직일 위치가 있다면 이동한다.
    else {
        curr_cell = best_pos;
        return true;
    }
}

int main() {
    cin >> n >> k;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    // 초기 위치를 설정한다.
    int r, c;
    cin >> r >> c;
    curr_cell = make_pair(r - 1, c - 1);

    // k번에 걸쳐 움직이는 것을 반복한다.
    while(k--) {
        bool is_moved = Move();

        // 움직이지 못했다면 바로 종료한다.
        if(!is_moved) break;
    }

    int final_x, final_y;
    tie(final_x, final_y) = curr_cell;
    cout << final_x + 1 << " " << final_y + 1 << endl;
}