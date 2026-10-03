#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int n, m;  // N, m

int a[10000005];
int b[10000005];
int a_idx = 1;
int b_idx = 1;

vector<pair<int, int>> a_move;
vector<pair<int, int>> b_move;

int CheckMeet() {
    for (int i = 1; i <= max(a_idx-1, b_idx-1); i++) {
        if (a[i] == b[i]) {
            return i;
        }
    }

    return -1;
}

int main() {
    cin >> n >> m;

    int t;
    char d;
    for (int i = 0; i < n; i++) {
        cin >> d >> t;
        a_move.push_back({d, t});
    }

    for (int i = 0; i < m; i++) {
        cin >> d >> t;
        b_move.push_back({d, t});
    }

    for (int i = 0; i < n; i++) {
        if (a_move[i].first == 'L'){
            for  (int j = 0; j < a_move[i].second; j++) {
                a[a_idx] = a[a_idx - 1] - 1;
                a_idx += 1;
            }  
        }
        if (a_move[i].first == 'R') {
            for (int j = 0; j < a_move[i].second; j++) {
                a[a_idx] = a[a_idx - 1] + 1;
                a_idx += 1;
            }
        }
    }

    for (int i = 0; i < m; i++) {
        if (b_move[i].first == 'L') {
            for (int j =0; j < b_move[i].second; j++) {
                b[b_idx] = b[b_idx - 1] - 1;
                b_idx += 1;
            }
        }

        if (b_move[i].first == 'R') {
            for (int j = 0; j < b_move[i].second; j++) {
                b[b_idx] = b[b_idx - 1] + 1;
                b_idx += 1;
            }
        }
    }   

    cout << CheckMeet() << endl;
    
    return 0;
}