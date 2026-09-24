#include <iostream>

using namespace std;

int a, b, c;

int main() {
    cin >> a >> b >> c; // 2011년 11월 11일 11시 11분 ~ 2011년 11월 a일 b시 c분

    // Please write your code here.
    // case1: A==11 -> 11일에서 시간의 차만큼 비교
    if (a == 11 && 11 <= b) {
        cout << (b * 60 + c) - (11 * 60 + 11) << endl;
    }
    // case2: A==12
    else if (a == 12) {
        cout << (12 * 60 + 49) + (b * 60 + c) << endl; 
    }
    // case3: A=>13
    else if (a >= 13) {
        cout << (12 * 60 + 49) + (a - 11 - 1) * 24 * 60 + (b * 60 + c) << endl;
    }
    else
        cout << -1 << endl;


    return 0;
}