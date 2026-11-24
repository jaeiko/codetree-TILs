#include <iostream>
#include <unordered_set>

using namespace std;

int n;
string command[100000];
int x[100000];

unordered_set<int> s;

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> command[i] >> x[i];
        if (command[i] == "add") {  // 추가
            s.insert(x[i]);
        } else if (command[i] == "remove") {    // 삭제
            s.erase(x[i]);
        } else if (command[i] == "find") {
            if (s.find(x[i]) != s.end()) {  // 집합 내에 존재하면 true
                cout << "true" << '\n';
            } else {    // 집합 내에 없으면 false
                cout << "false" << '\n';
            }
        }
    }

    return 0;
}
