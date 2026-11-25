#include <iostream>
#include <algorithm>
#include <climits>
#include <vector>

using namespace std;

int n, s;
vector<int> arr;

int slidingWindowMinLength(const vector<int>& arr, int targetSum) {
    int left = 0;
    int currentSum = 0;
    int minLength = INT_MAX;

    for (int right = 0; right < (int)arr.size(); right++) {
        currentSum += arr[right];

        while (currentSum >= targetSum && left <= right) {
            minLength = min(minLength, right - left + 1);
            currentSum -= arr[left];
            left++;
        }
    }

    return minLength != INT_MAX ? minLength : -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> s;
    arr.resize(n);

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Please write your code here.
    cout << slidingWindowMinLength(arr, s);

    return 0;
}