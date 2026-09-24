#include <iostream>
#include <cmath>
#include <climits>

using namespace std;

int N, S;
int arr[100];

int sum = 0;
int cal = 0;
int min_diff = INT_MAX;

int main() {
    cin >> N >> S;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
        sum += arr[i];
    }

    // Please write your code here.
    for (int i = 0; i < N-1; i++) {
        for (int j = i + 1; j < N; j++) {
            cal = sum - arr[i] - arr[j];
            if (abs(S-cal) < min_diff) min_diff = abs(S - cal);
            cal = sum;
        }
    }

    cout << min_diff << endl;

    return 0;
}