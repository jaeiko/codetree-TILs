#include <iostream>

using namespace std;

int N;
char dir[100];
int dist[100];

int curr_x = 0, curr_y = 0;

int time_count = 0;

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> dir[i] >> dist[i];

        for (int j = 0; j < dist[i]; j++) {
            if (dir[i] == 'N') curr_x += dx[1];
            else if (dir[i] == 'E') curr_y += dy[2];
            else if (dir[i] == 'S') curr_x += dx[0];
            else curr_y += dy[3];

            time_count++;

            if (curr_x == 0 && curr_y == 0) {
                cout << time_count << endl;
                return 0;
            }
        }
    }

    // Please write your code here.
    cout << -1 << endl;

    return 0;
}