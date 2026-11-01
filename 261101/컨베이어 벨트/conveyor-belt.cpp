#include <iostream>
#include <vector>

using namespace std;

int n, t;

int main() {
    cin >> n >> t;
    vector<int> arr(n * 2); // 항상 벡터는 n 입력받은 후에 선언할 수 있다.
    // int arr[] 에서 [] 안에는 상수만 가능하니 벡터를 잘 활용하자.

    for (int i = 0; i < n; i++) cin >> arr[i];

    for (int i = n; i < n*2; i++) cin >> arr[i];

    // Please write your code here.

    int temp = 0;

    // t만큼 옮기기
    for (int i = 0; i < t; i++) {
        // 우선 가장 마지막 원소값을 temp에 저장
        temp = arr[n*2 - 1];
        for (int j = n*2 - 1 ; j > 0; j--) {
            arr[j] = arr[j-1];
        }
        arr[0] = temp;
    }

    // 출력
    for (int i = 0; i < n; i++) cout << arr[i] << ' ';
    cout << endl;
    for (int i = n; i < n*2; i++) cout << arr[i] << ' ';

    return 0;
}
