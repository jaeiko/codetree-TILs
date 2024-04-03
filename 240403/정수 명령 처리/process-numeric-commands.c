#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define _CRT_SECURE_NO_WARNINGS
#define MAX_STACK 1000000

typedef enum { false, true } bool;
typedef int Data;

typedef struct {
    Data items[MAX_STACK];
    int top;
} Stack;

// Make stack empty.
void InitStack(Stack* pstack);
// Check whether stack is full
bool IsFull(Stack* pstack);
// Check whether stack is empty
bool IsEmpty(Stack* pstack);

// Read the item at the top
Data Peek(Stack* pstack);
// Insert an item at the top
void Push(Stack* pstack, Data item);
// Remove the item at the top
void Pop(Stack* pstack);

int main() {
    int count;
    char command[10];
    int num;
    Stack stack;
    InitStack(&stack);
    scanf("%d", &count);

    for (int i = 0; i < count; i++) {
        char command[10];
        scanf("%s", command);

        if (strcmp(command, "push") == 0) {
            scanf(" %d", &num);
            Push(&stack, num);
        }
        else if (strcmp(command, "pop") == 0) {
            if (!IsEmpty(&stack)) {
                Data poppedItem = Peek(&stack);
                Pop(&stack);
                printf("%d\n", poppedItem);
            }
        }
        else if (strcmp(command, "size") == 0) {
            printf("%d\n", stack.top + 1);
        }
        else if (strcmp(command, "top") == 0) {
            if (!IsEmpty(&stack)) {
                printf("%d\n", Peek(&stack));
            }
        }
        else if (strcmp(command, "empty") == 0) {
            if (IsEmpty(&stack)) {
                printf("1\n");
            }
            else {
                printf("0\n");
            }
        }
    }
    return 0;
}

void InitStack(Stack* pstack) {
    pstack->top = -1;
}

bool IsFull(Stack* pstack) {
    return pstack->top == MAX_STACK - 1;
}

bool IsEmpty(Stack* pstack) {
    return pstack->top == -1;
}

Data Peek(Stack* pstack) {
    if (IsEmpty(pstack)) {
        return -1;    // error: empty stack
    }
    return pstack->items[pstack->top];
}

void Push(Stack* pstack, Data item) {
    if (IsFull(pstack)) {
        return;    // error: stack full
    }
    pstack->items[++(pstack->top)] = item;
}

void Pop(Stack* pstack) {
    if (IsEmpty(pstack)) {
        return;   // error: empty stack
    }
    --(pstack->top);
}