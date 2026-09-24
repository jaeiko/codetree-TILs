#include <iostream>
#include <cmath>
#include <climits>

using namespace std;

int n;
int x[100];
int y[100];

int min_dis = INT_MAX;
int dist = 0;

int cnt = 0;

int main() {
    cin >> n;   // 체크포인트 개수
    for (int i = 0; i < n; i++) {
        cin >> x[i] >> y[i];
    }

    // Please write your code here.
    // 첫 체크포인트, 마지막 체크포인트는 제외
    for (int i = 1; i < n-1; i++) {
        // index i에 있는 체크포인트를 제외한 나머지 체크포인트 근접한 좌표들은 맨하탄 거리에 누적해서 더함
        for (int j = 0; j < n-1; j++) {
            if (j == i || j+1 == i){        // j = i이거나 j+1 = i인 경우 한칸 건너뛰어 맨하탄거리 계산
                dist += (abs(x[j] - x[j+2]) + abs(y[j] - y[j+2]));
                j += 1;
            }
            else
                dist += (abs(x[j] - x[j+1]) + abs(y[j] - y[j+1]));
        }
        if (dist < min_dis) min_dis = dist;
        dist = 0;
    }

    cout << min_dis << endl;
    return 0;
}