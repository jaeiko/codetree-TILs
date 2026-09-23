#include <iostream>

using namespace std;

int m1, d1, m2, d2; // m1월 d1일 ~ m2월 d2일

// 아래처럼 앞에 0을 추가로 둬서 인덱스를 월 형식으로 쉽게 가자.
int month[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

int elapsed_days = 0;

int main() {
    cin >> m1 >> d1 >> m2 >> d2;

    // Please write your code here.
    for (int i = m1+1; i < m2; i++) {
        // m1, m2 사이에 있는 월들의 총 날들을 더함.
        elapsed_days += month[i];
    }

    // m1, m2의 남은 날들을 더함.
    if (m1 != m2)
        elapsed_days += (month[m1] - d1 + 1) + d2;
    else
        elapsed_days = d2-d1+1;

    cout << elapsed_days << endl;
    return 0;
}