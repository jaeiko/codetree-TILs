#include <iostream>
#include <algorithm>
#define OFFSET 100 

using namespace std;

int n;
int x1[100], x2[100];
int load[1000] = {0};

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> x1[i] >> x2[i];
        x1[i] += OFFSET;
        x2[i] += OFFSET;

        for (int j = x1[i]; j < x2[i]; j++){
            load[j] += 1;
        }
    }

    int load_size = sizeof(load) / sizeof(load[0]);

    // Please write your code here.
    int max_val = *max_element(load, load + load_size);

    cout << max_val << endl;


    return 0;
}