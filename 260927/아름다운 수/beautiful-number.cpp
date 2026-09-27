#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> answer;
int total_count = 0;    // 아름다운 수의 총 개수

// 연속 블록 검증 함수
bool CheckBeautiful() {
    for (int i = 0; i < n; ) {
        int target = answer[i];

        // target만큼 연속할 공간이 뒤에 남아있지 않으면 탈출
        if (i + target > n) return false;

        // i부터 i + target - 1까지 모두 target과 같은지 검사
        for (int j = i; j < i + target; j++) {
            if (answer[j] != target) return false;
        }

        // 핵심: 유효하다면 target칸만큼 건너뛰어 다음 블록 확인
        i += target;
    }
    return true;
}


// curr_num: 현재 자릿수
void Choose(int curr_num) {
    // 1. n자리가 완성되었으면 유효성을 검사하고 "무조건 종료"
    if (curr_num == n) {
        if (CheckBeautiful()) {
            total_count++;
        }
        return; // 무조건 return 하여 무한 재귀 차단
    }

    // 2. 1~4 숫자 선택 및 백트래킹
    for (int select = 1; select <= 4; select++) {
        answer.push_back(select);
        Choose(curr_num + 1);
        answer.pop_back();
    }
}

int main() {
    cin >> n;

    // Please write your code here.

    Choose(0);

    cout << total_count << endl;

    return 0;
}
