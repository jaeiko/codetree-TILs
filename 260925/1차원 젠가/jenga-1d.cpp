#include <iostream>

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
    cin >> n;   // 블록의 수 입력
    // 위에서부터 맨 아래까지 순서대로 각 층에 놓여있는 블록에다가 정수 입력
    for (int i = 0; i < n; i++) {
        cin >> blocks[i];
    }

    cin >> s1 >> e1;    // s1 ~ e1 블럭 빼기
    cin >> s2 >> e2;    // s2 ~ e2 블럭 빼기

    // Please write your code here.
    // s1 ~ e1 블럭 빼기
    for (int i = 0; i < n; i++) {
        // index s1일 때 e1으로 넘기기
        if (i == s1-1) {
            i = e1;
            // cout << "if문 안의 i: " << i << endl;
        }
        // cout << "if문 바깥의 i: " << i << endl;
        temp1[temp1_end] = blocks[i];
        // cout << "temp1_end: " << temp1_end << endl;
        // cout << "temp1[temp1_end]: " << temp1[temp1_end] << endl;
        temp1_end += 1;
    }

    // cout << "temp1_end: " << temp1_end << endl;
    // cout << "temp1[0]: " << temp1[0] << endl;
    // cout << "temp1[1]: " << temp1[1] << endl;

    // s2 ~ e2 블럭 빼기
    for (int i = 0; i < temp1_end; i++) {
        if (i == s2-1) {
            i = e2;
        }
        if (temp1[i] == 0) {
            break;
        }
        temp2[temp2_end] = temp1[i];
        temp2_end += 1;
        // cout << "temp2[temp2_end]: " << temp2[temp2_end] << endl;
    }

    // cout << "temp2_end: " << temp2_end << endl;

    if (temp2[0] != 0) 
        cout << temp2_end << endl;
    else cout << 0 << endl;

    for (int i = 0; i < temp2_end; i++) {
        cout << temp2[i] << endl;
    }

    return 0;
}
