#include <bits/stdc++.h>

using namespace std;

int n;
int blocks[100];
int s1, e1;
int s2, e2;

int temp1[100];
int temp2[100];

int temp1_end = 0;
int temp2_end = 0;

int main() {
    cin >> n;       // 블록의 수 입력
    // 위에서부터 맨 아래까지 순서대로 각 층에 놓여있는 블록에다가 정수 입력
    for (int i = 0; i < n; i++) {
        cin >> blocks[i];
    }

    cin >> s1 >> e1;
    cin >> s2 >> e2;

    // s1 ~ e1 블럭 빼기
    for (int i = 0; i < n; i++) {
        if (i == s1 - 1) {
            i = e1;
        }

        temp1[temp1_end] = blocks[i];
        temp1_end += 1;
    }

    // s2 ~ e2 블럭 빼기
    for (int i = 0; i < temp1_end; i++) {
        if (i == s2 - 1) {
            i = e2;
        }
        // 만약 블록값 0이면 더이상 들어온 값 없으니 반복문 탈출
        if (temp1[i] == 0) {
            break;
        }
        temp2[temp2_end] = temp1[i];
        temp2_end += 1;
    }

    // 만약 temp2의 첫번째 값이 0이 아니라면 크기 출력, 만약 0이면 크기 0 출력
    if (temp2[0] != 0) cout << temp2_end << endl;
    else cout << 0 << endl;

    for (int i = 0; i < temp2_end; i++) {
        cout << temp2[i] << endl;
    }

    return 0;
}