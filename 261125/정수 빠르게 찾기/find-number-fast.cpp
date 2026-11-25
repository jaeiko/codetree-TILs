#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n, m, idx;
vector<int> arr;
vector<int> queries;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> m;
    arr.resize(n);
    queries.resize(m);

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // 이분탐색을 위해 정렬
    sort(arr.begin(), arr.end());

    for (int i = 0; i < m; i++) {
        cin >> queries[i];
    }

    // Please write your code here.
    for (int i = 0; i < m; i++) {
        idx = lower_bound(arr.begin(), arr.end(), queries[i]) - arr.begin();
        if (idx < (int)arr.size() && arr[idx] == queries[i]) {
            cout << idx + 1 << "\n";
        } else {
            cout << -1 << "\n";
        }

    }

    return 0;
}