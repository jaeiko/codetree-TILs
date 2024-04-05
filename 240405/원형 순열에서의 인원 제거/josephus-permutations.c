// Queue 문제
// 요세푸스 문제

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_QUEUE 100

typedef enum { false, true } bool;
typedef int Data;

typedef struct {
    int front, rear, size;
    Data items[MAX_QUEUE];
}Queue;

// Make a queue empty.
void InitQueue(Queue* pqueue);
// Check whether a queue is full.
bool IsFull(Queue* pqueue);
// Check whether a queue is empty.
bool IsEmpty(Queue* pqueue);

// Read the item at the front.
Data Peek(Queue* pqueue);
// Insert an item at the rear.
void EnQueue(Queue* pqueue, Data item);
// Delete an item at the front.
void DeQueue(Queue* pqueue);

// 원형 순열에서의 인원 제거하는 함수
void solution(int n, int k);

int main() {
    int n, k;   // n : n명의 사람 | k : k번째 사람 제거
    scanf("%d %d", &n, &k);
    solution(n, k);

    return 0;
}

// 원형 순열에서의 인원 제거하는 함수
void solution(int n, int k) {
    Queue queue;
    InitQueue(&queue);
    for (int i = 1; i <= n; i++) {
        EnQueue(&queue, i);
    }
    // 마지막 1명 남을 때까지 1번부터 순서대로 k번째 사람 제거
    while (queue.size != 1) {
        for (int i = 1; i < k; i++) {   // k - 1번째 사람까지 반복
            EnQueue(&queue, Peek(&queue));  // k번째보다 앞에 있는 사람들은 순차적으로 1명씩 Enqueue 후 Dequeue
            DeQueue(&queue);
        }
        // k 번째 사람은 출력 후 Dequeue해서 queue에 요소 제거
        int dequeuedItem = Peek(&queue);
        DeQueue(&queue);
        printf("%d ", dequeuedItem);
    }
}

// Make a queue empty.
void InitQueue(Queue* pqueue) {
    pqueue->front = pqueue->rear = 0;
}
// Check whether a queue is full.
bool IsFull(Queue* pqueue) {
    return pqueue->front == (pqueue->rear + 1) % MAX_QUEUE;
}
// Check whether a queue is empty.
bool IsEmpty(Queue* pqueue) {
    return pqueue->front == pqueue->rear;
}
// Read the item at the front.
Data Peek(Queue* pqueue) {
    if (IsEmpty(pqueue))
        exit(1);    // error: empty queue
    return pqueue->items[pqueue->front];
}
// Insert an item at the rear.
void EnQueue(Queue* pqueue, Data item) {
    if (IsFull(pqueue))
        exit(1);    // error: queue full
    pqueue->items[pqueue->rear] = item;
    pqueue->rear = (pqueue->rear + 1) % MAX_QUEUE;
    pqueue->size += 1;
}
// Delete an item at the front.
void DeQueue(Queue* pqueue)
{
    if (IsEmpty(pqueue))
        exit(1);    // error: empty queue
    pqueue->front = (pqueue->front + 1) % MAX_QUEUE;
    pqueue->size -= 1;
}