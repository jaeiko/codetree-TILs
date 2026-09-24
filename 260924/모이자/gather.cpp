#include <iostream>
#include <climits>  // INT_MIN ,INT_MAX 사용하기 위함.
#include <cstdlib>  // abs
#include <algorithm>// max

using namespace std;

int min_val = INT_MAX;
int dist = 0;   // distance는 iostream 헤더 안에 있을 수 있으니 피하자

int n;
int A[100]; // 각 집에 살고 있는 사람의 수

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    // Please write your code here.
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist += abs(j - i) * A[j];
        }
        if (dist < min_val) min_val = dist;
        dist = 0;
    }

    cout << min_val << endl;

    return 0;
}