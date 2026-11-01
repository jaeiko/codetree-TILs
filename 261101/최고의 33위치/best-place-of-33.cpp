#include <bits/stdc++.h>

using namespace std;

int N;
int grid[20][20];

int cnt = 0;
int max_val = INT_MIN;

bool InRange(int x, int y) {
    return 0 <= x && x < N && 0 <= y && y < N;
}

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> grid[i][j];
        }
    }

    // Please write your code here.
    for (int x = 0; x < N; x++) {
        for (int y = 0; y < N; y++) {
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    if(!InRange(x+i, y+i)){
                        cnt = 0;
                        continue;
                    }
                    if (grid[x+i][y+j] == 1) cnt += 1;
                }
            }
            max_val = max(max_val, cnt);
            cnt = 0;
        }
    }

    cout << max_val << endl;

    return 0;
}
