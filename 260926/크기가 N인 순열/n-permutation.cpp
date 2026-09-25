#include <iostream>
#include <vector>

using namespace std;

int n;  // 1~n까지의 수
vector<int> answer;
vector<bool> visited(n+1);

void PrintAnswer() {
    for (int i = 0; i < answer.size(); i++) cout << answer[i] << " ";
    cout << endl;
}

void Choose(int curr_num) {
    if (curr_num == n + 1) {
        PrintAnswer();
        return;
    }

    for (int i = 1; i <= n; i++) {
        if (visited[i]) continue;

        visited[i] = true;
        answer.push_back(i);

        Choose(curr_num + 1);

        answer.pop_back();
        visited[i] = false;

    }
}

int main() {
    cin >> n;

    // Please write your code here.
    Choose(1);
    return 0;
}
