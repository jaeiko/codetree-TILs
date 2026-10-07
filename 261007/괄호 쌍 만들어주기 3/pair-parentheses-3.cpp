#include <iostream>
#include <string>

using namespace std;

string A;

int count = 0;

int main() {
    cin >> A;

    // Please write your code here.
    for (int i = 0; i < A.length(); i++) {
        for (int j = i+1; j < A.length(); j++) {
            if (A[i] == '(' && A[j] ==')') count += 1;
        }
    }

    cout << count << endl;

    return 0;
}