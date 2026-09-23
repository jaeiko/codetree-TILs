#include <iostream>

using namespace std;

int a, b, c, d; // a시 b분 ~ c시 d분

int main() {
    cin >> a >> b >> c >> d;

    // Please write your code here.
    cout << (c * 60 + d) - (a * 60 + b) << endl;
    
    return 0;
}