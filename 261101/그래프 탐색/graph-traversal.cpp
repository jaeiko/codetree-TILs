#include <bits/stdc++.h>

using namespace std;

int n, m;
int from[10000], to[10000];
int cnt = 0;

// 그래프
int graph[1001][1001] = {};

bool visited[1500] = {};

void DFS(int vertex) {
    for (int curr_v = 1; curr_v <= n; curr_v++) {
        if (graph[vertex][curr_v] && !visited[curr_v]) {
            visited[curr_v] = true;
            cnt += 1;
            DFS(curr_v);
        }
    }
}

int main() {
    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        cin >> from[i] >> to[i];
        graph[from[i]][to[i]] = 1;
        graph[to[i]][from[i]] = 1;
    }

    // Please write your code here.
    
    visited[1] = true;
    DFS(1);

    cout << cnt << endl;

    return 0;
}
