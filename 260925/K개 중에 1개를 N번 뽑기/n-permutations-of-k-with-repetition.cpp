#include <iostream>
#include <vector>

using namespace std;

int K, N;   // 1~K 이하의 정수를 하나 고르는 행위를 N번 반복.
vector<int> answer; // 크기가 0인 빈 벡터

void PrintAnswer() {
    for (int i = 0; i < answer.size(); i++) cout << answer[i] << " ";
    cout << endl;
}

// curr_num번째 위치에 0 혹은 1을 선택하는 함수
void Choose(int curr_num, int n, int k) {
    // 종료 조건
    if (curr_num == n) {
        PrintAnswer();
        return;
    }

    // 반복문을 이용해 1, 2, ..., K을 선택했을 때 재귀 호출
    for (int select = 1; select <= K; select++) {
        answer.push_back(select);
        Choose(curr_num + 1, n, k);
        answer.pop_back();
    }
}

int main() {
    cin >> K >> N;

    // Please write your code here.
    Choose(0, N, K);

    return 0;
}
