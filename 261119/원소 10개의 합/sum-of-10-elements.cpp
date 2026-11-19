#include <iostream>
using namespace std;

int arr[10];
int sum_val = 0;

int main() {
    // Please write your code here.
    for (int i = 0; i < 10; i++) {
        cin >> arr[i];

        sum_val += arr[i];
    }

    cout << sum_val << endl;
    return 0;
}