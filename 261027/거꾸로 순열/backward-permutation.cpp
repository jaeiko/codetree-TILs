#include <iostream>
#include <vector>

using namespace std;

int n;
bool visited[9];
vector<int> answer;

void PrintAnswer() {
    for (int i = 0; i < answer.size(); i++)
        cout << answer[i] << " ";
    cout << endl;
}

void Choose(int curr_num) {
    if (curr_num == n + 1) {
        PrintAnswer();
        return;
    }

    for (int i = n; i >= 1; i--) {
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
