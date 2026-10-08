#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int n;
int grid[20][20];

// 폭탄이 위치한 좌표들을 저장하는 벡터
vector<pair<int, int>> bomb_pos;

// 각 폭탄에 할당된 폭탄 유형을 저장하는 벡터 (0: 세로, 1: 십자, 2: X자)
vector<int> selected_types;

int max_exploded_cnt = 0;

// 각 폭탄 유형별 폭발 상대 좌표 오프셋(자기 자신 포함 5칸)
// type 0: 세로 폭탄 (상하 2칸씩)
// type 1: 십자 폭탄 (상하좌우 1칸씩)
// type 2: X자 폭탄 (대각선 1칸씩)
pair<int, int> bomb_shapes[3][5] = {
    {{-2, 0}, {-1, 0}, {0, 0}, {1, 0}, {2, 0}},
    {{-1, 0}, {1, 0}, {0, 0}, {0, -1}, {0, 1}},
    {{-1, -1}, {-1, 1}, {0, 0}, {1, -1}, {1, 1}}
};

bool InRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < n;
}

// 선택된 폭탄 조합으로 초토화되는 칸의 합집합 크기 계산
int CalculateArea() {
    bool exploded[20][20] = {false};
    int total_cnt = 0;

    for (int i = 0; i < (int)bomb_pos.size(); i++) {
        int x = bomb_pos[i].first;
        int y = bomb_pos[i].second;
        int type = selected_types[i];

        for (int dir = 0; dir < 5; dir++) {
            int nx = x + bomb_shapes[type][dir].first;
            int ny = y + bomb_shapes[type][dir].second;

            if (InRange(nx, ny) && !exploded[nx][ny]) {
                exploded[nx][ny] = true;
                total_cnt++;
            }
        }
    }
    return total_cnt;
}

// 백트래킹을 통해 모든 폭탄의 조합을 시도
void FindMaxArea(int bomb_idx) {
    // 모든 폭탄의 종류가 결정된 경우 (기저 조건)
    if (bomb_idx == (int) bomb_pos.size()) {
        max_exploded_cnt = max(max_exploded_cnt, CalculateArea());
        return;
    }

    // 현재 폭탄(bomb_idx)에 대해 3가지 폭탄 종류를 순차적으로 시도
    for (int type = 0; type < 3; type++) {
        selected_types.push_back(type);
        FindMaxArea(bomb_idx + 1);
        selected_types.pop_back();  // 백트래킹 상태 복원
    }
}

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
            if (grid[i][j] == 1) {
                bomb_pos.push_back({i, j});
            }
        }
    }

    // 폭탄이 하나도 없는 예외 케이스 처리
    if (bomb_pos.empty()) {
        cout << 0 << endl;
        return 0;
    }

    FindMaxArea(0);

    cout << max_exploded_cnt << endl;

    return 0;
}