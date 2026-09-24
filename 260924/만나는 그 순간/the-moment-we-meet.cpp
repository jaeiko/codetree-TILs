#include <iostream>
#include <cstdlib>  // exit, EXIT_SUCCESS
#include <algorithm>

using namespace std;

int n, m;
char d[1000];
int t[1000];
char d2[1000];
int t2[1000];

int A[1000050] = {0};
int A_index = 0;
int A_move = 0;

int B[1000050] = {0};
int B_index = 0;
int B_move = 0;

int main() {
    cin >> n >> m;

    // n개의 줄을 거쳐 각 줄마다 A가 어떤 방향으로 몇 초동안 이동했는지 나타내는 (d, t)가 공백 사이에 두고 주어짐.
    for (int i = 0; i < n; i++) {
        cin >> d[i] >> t[i];
        if (d[i] == 'L') {
            for (int j = 1; j <= t[i]; j++) {
                A_index += 1;
                A[A_index] = A[A_index - 1] - 1;
                A_move += 1;
            }
        }
        else if (d[i] == 'R') {
            for (int j = 1; j <= t[i]; j++) {
                A_index += 1;
                A[A_index] = A[A_index - 1] + 1;
                A_move += 1;
            }
        }
    }

    // m개의 줄을 걸쳐 각 줄마다 B가 어떤 방향으로 몇 초동안 이동했는지 나타내는 (d, t)가 같은 형식으로 주어짐.
    for (int i = 0; i < m; i++) {
        cin >> d2[i] >> t2[i];

        if (d2[i] == 'L') {
            for (int j = 1; j <= t2[i]; j++) {
                B_index += 1;
                B[B_index] = B[B_index - 1] - 1;
                B_move += 1;
            }
        }
        else if (d2[i] == 'R') {
            for (int j = 1; j <= t2[i]; j++) {
                B_index += 1;
                B[B_index] = B[B_index - 1] + 1;
                B_move += 1;
            }
        }
    }

    

    // Please write your code here.
    for (int i = 1; i <= max(A_move, B_move); i++) {
        if (A[i] == B[i]){
            cout << i << endl;
            exit(0);
        }
    }

    cout << -1 << endl;

    return 0;
}