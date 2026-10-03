#include <iostream>
#include <vector>

using namespace std;

int N, M;
vector<int> answer;

void PrintAnswer() {
    for (int i = 0; i < M; i++) {
        cout << answer[i] << " ";
    }
    cout << "\n";
}

// curr_num: 현재까지 선택한 숫자의 개수
// last_num: 가장 최근에 선택한 숫자 (다음에 선택할 숫자의 하한선)
void Choose(int curr_num, int last_num) {
    // M개를 모두 선택했다면 출력 후 종료
    if (curr_num == M) {
        PrintAnswer();
        return;
    }

    // 직전에 선택한 수(last_num)보다 큰 수만 선택
    for (int select = last_num + 1; select <= N; select++) {
        answer.push_back(select);
        Choose(curr_num + 1, select);   // 방금 선택한 숫자를 last_num으로 전달
        answer.pop_back();  // 상태 원복 (Backtracking)
    }
}

int main() {
    cin >> N >> M;

    // 0개를 선택했고, 아직 아무것도 선택하지 않았으므로 last_num은 0
    Choose(0, 0);

    return 0;
}