#include <iostream>
#include <string>
using namespace std;

// 노드 구조체
struct Node {
    string data;    // 노드 하나에 문자열 하나
    Node *prev, *next;  // 이전 | 다음 노드 포인터

    Node(const string& value)
        : data(value), prev(nullptr), next(nullptr) {}
};

// 1번: 현재 노드 앞에 삽입
void InsertPrev(Node *u, Node *node) {
    // 새 노드(node)의 연결 정보 설정
    node->prev = u->prev;
    node->next = u;

    // 기존 왼쪽 노드의 다음 노드를 변경
    if (u->prev != nullptr) {
        u->prev->next = node;
    }

    // 현재 노드의 이전 노드를 변경
    u->prev = node;
}

// 2번: 현재 노드 뒤에 삽입
void InsertNext(Node *u, Node *node) {
    // 새 노드의 연결 정보 설정
    node->next = u->next;
    node->prev = u;

    // 기존 오른쪽 노드의 이전 노드를 변경
    if (u->next != nullptr) {
        u->next->prev = node;
    }

    // 현재 노드의 다음 노드를 변경
    u->next = node;
}

void Print(Node *u) {
    // 이전 노드
    if (u->prev != nullptr) cout << u->prev->data;
    else cout << "(Null)";

    // 현재 노드
    cout << ' ' << u->data << ' ';

    // 다음 노드
    if (u->next != nullptr) cout << u->next->data;
    else cout << "(Null)";

    cout << '\n';
}

string S_init;
int N;
int command[250000];
string S_value[250000];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> S_init;
    cin >> N;

    // 전체 명령 입력
    for (int i = 0; i < N; i++) {
        cin >> command[i];
        if (command[i] == 1 || command[i] == 2) {
            cin >> S_value[i];
        }
    }

    // Please write your code here.

    //최초 노드 생성
    Node *curr = new Node(S_init);

    // 명령 순서대로 수행
    for (int i = 0; i < N; i++) {
        // 1, 2번: 삽입할 문자열로 노드 생성
        if (command[i] == 1 || command[i] == 2) {
            Node *node = new Node(S_value[i]);

            if (command[i] == 1) {
                // 현재 노드 앞에 삽입
                InsertPrev(curr, node);
            }
            else {
                // 현재 노드 뒤에 삽입
                InsertNext(curr, node);
            }
            // 삽입 후에도 curr은 유지
        }
        else if (command[i] == 3) {
            // 3번: 이전 노드가 있으면 이동
            if (curr->prev != nullptr) {
                curr = curr->prev;
            }
        }
        else if (command[i] == 4) {
            // 4번: 다음 노드가 있으면 이동
            if (curr->next != nullptr) {
                curr = curr->next;
            }
        }

        // 모든 명령 직후 출력
        Print(curr);
    }

    // 동적 할당한 노드 메모리 해제
    Node *head = curr;

    // 첫 노드까지 이동
    while (head->prev != nullptr) {
        head = head->prev;
    }

    // 첫 노드부터 순서대로 해제
    while (head != nullptr) {
        Node *next = head->next;
        delete head;
        head = next;
    }

    return 0;
}
