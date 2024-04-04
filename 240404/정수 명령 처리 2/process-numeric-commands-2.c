/*
Queue 문제

정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define _CRT_SECURE_NO_WARNINGS
#define MAX_QUEUE 100000

typedef enum { false, true } bool;
typedef int Data;

typedef struct {
    int front, rear;
    Data items[MAX_QUEUE];
} Queue;

// Make a queue empty.
void InitQueue(Queue* pqueue);
// Check whether q queue is full.
bool IsFull(Queue* pqueue);
// Check whether a queue is empty.
bool IsEmpty(Queue* pqueue);

// Read the item at the front.
Data Peek(Queue* pqueue);
// Calculate the size of the queue.
Data Size(Queue* pqueue);
// Insert an item at the rear.
void EnQueue(Queue* pqueue, Data item);
// Delete an item at the front.
void DeQueue(Queue* pqueue);

int main() {
    int count, num; // count : 반복 횟수 | num : push할 정수
    char command[10];   // 명령어 입력 변수

    // Queue 생성
    Queue queue;
    InitQueue(&queue);
    
    scanf("%d", &count);

    
    for (int i = 0; i < count; i++) {
        scanf("%s", command);
        if (strcmp(command, "push") == 0) { // push 실행
            scanf("%d", &num);
            EnQueue(&queue, num);
        }
        else if (strcmp(command, "pop") == 0) { // pop 실행
            if (!IsEmpty(&queue)) {
                Data dequeuedItem = Peek(&queue);
                DeQueue(&queue);
                printf("%d\n", dequeuedItem);
            }
        }
        else if (strcmp(command, "size") == 0) {    // queue size 체크
            printf("%d\n", Size(&queue));
        }
        else if (strcmp(command, "front") == 0) {   // queue의 front 부분 체크
            printf("%d\n", Peek(&queue));
        }
        else if (strcmp(command, "empty") == 0) {   // queue가 비워져 있는지 체[크]
            if (IsEmpty(&queue)) {
                printf("1\n");  // 비워져 있으면 1 출력
            }
            else {
                printf("0\n");  // 요소가 있다면 0 출력
            }
        }
    }
    return 0;
}

// Make a queue empty.
void InitQueue(Queue* pqueue) {
    pqueue->front = pqueue->rear = 0;
}

// Check whether a queue is full.
bool IsFull(Queue* pqueue) {
    return pqueue->front == (pqueue->rear + 1) % MAX_QUEUE;
}

// CHeck whether a queue is empty.
bool IsEmpty(Queue* pqueue) {
    return pqueue->front == pqueue->rear;
}

// Read the item at the front.
Data Peek(Queue* pqueue) {
    if (IsEmpty(pqueue))
        exit(1);    // error: empty stack
    return pqueue->items[pqueue->front];
}

// Calculate the size of the queue.
Data Size(Queue* pqueue) {
    return (pqueue->rear - pqueue->front + MAX_QUEUE) % MAX_QUEUE;
}

// Insert an item at the rear.
void EnQueue(Queue* pqueue, Data item) {
    if (IsFull(pqueue))
        exit(1);    // error: stack full
    pqueue->items[pqueue->rear] = item;
    pqueue->rear = (pqueue->rear + 1) % MAX_QUEUE;
}

// Delete an item at the front.
void DeQueue(Queue* pqueue) {
    if (IsEmpty(pqueue))
        exit(1);    // error: empty stack
    pqueue->front = (pqueue->front + 1) % MAX_QUEUE;
}