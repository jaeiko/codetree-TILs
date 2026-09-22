#include <iostream>
#include <algorithm>

using namespace std;

int N, K;
int A[100], B[100];

int main() {
    cin >> N >> K;
    int total[N] = {0}; // 크기가 N인 배열의 모든 요소를 0으로 초기화

    for (int i = 0; i < K; i++) {
        cin >> A[i] >> B[i];
        for (int j = A[i]-1; j < B[i]; j++){
            total[j] += 1;
        }
    }

    int size = sizeof(total) / sizeof(total[0]);

    // Please write your code here.
    int max_val = *max_element(total, total + size);

    cout << max_val << endl;

    return 0;
}