#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> arr;
vector<int> sorted_arr;

vector<int> bubble_sort(vector<int> arr, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i; j++) {
            if (arr[j] > arr[j+1] && arr[j] != 0 && arr[j+1] != 0) {
                int tmp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = tmp;
            }
        }
    }

    return arr;
}

int main() {
    cin >> n;
    arr.resize(n);

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Please write your code here.
    sorted_arr = bubble_sort(arr, n);

    for (int i = 0; i < n; i++) {
        cout << sorted_arr[i] << ' ';
    }

    return 0;
}
