#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int N;
int max_val = INT_MIN;

bool InRange(int x, int y, int n) {
    return 0 <= x && x < n && 0 <= y && y < n;
}

int cnt = 0;

int main() {
    cin >> N;
    vector <vector<int>> grid(N, vector<int>(N));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> grid[i][j];
        }
    }

    // Please write your code here.

    for (int x = 0; x < N; x++) {
        for (int y = 0; y < N; y++) {

            for (int i = 0; i < 3; i++){
                for (int j = 0; j < 3; j++) {
                    if (!InRange(x+i, y+j, N)) {
                        cnt = 0;
                        continue;
                    }
                    if (grid[x+i][y+j] == 1) cnt += 1;
                }
            }
            if (max_val < cnt) {
                max_val = cnt;
            }
            cnt = 0;
        }
    }

    cout << max_val << endl;

    return 0;
}
