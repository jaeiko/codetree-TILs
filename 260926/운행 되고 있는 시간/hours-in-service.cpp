#include <iostream>
#include <climits>
#include <vector>
#include <algorithm>

using namespace std;

int N;  // 개발자 N명
int A[100], B[100];           // 일하는 시간 (A~B시간)
int mid_result;               // 한 개발자를 제외한 나머지 모든 개발자들의 일하는 시간을 더해 저장한 변수
int max_sum = INT_MIN;        // 최종 결과값

vector<int> result;

int except_index = 0;

int main() {
    cin >> N;
    result.assign(1000, 0);

    for (int i = 0; i < N; i++) {
        cin >> A[i] >> B[i];
    }

    // Please write your code here.
    while (except_index < N) {
        for (int i = 0; i < N; i++) {
            if (except_index == i) continue;
            for (int j = A[i]; j < B[i]; j++) {
                result[j] = 1;
            }
        }

        int cnt = count(result.begin(), result.end(), 1);
        if (cnt > max_sum) max_sum = cnt;

        except_index++;
        result.assign(1000, 0);
    }

    cout << max_sum << endl;

    return 0;
}