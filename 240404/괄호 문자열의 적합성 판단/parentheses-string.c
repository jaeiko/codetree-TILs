/*
Stack 문제

입력으로 주어진 괄호 문자열의 짝이 올바른지, 그렇지 못한지를 판단하여 결과를 출력하는 프로그램
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define _CRT_SECURE_NO_WARNINGS
#define MAX_STACK 100

typedef enum { false, true } bool;
typedef int Data;

typedef struct {
	Data items[MAX_STACK];
	int top;
} Stack;

// Make stack empty.
void InitStack(Stack* pstack);
// Check whether stack is full.
bool IsFull(Stack* pstack);
// Check whether stack is empty.
bool IsEmpty(Stack* pstack);

// Read the item at the top.
Data Peek(Stack* pstack);
// Insert an item at the top.
void Push(Stack* pstack, Data item);
// Remove the item at the top.
void Pop(Stack* pstack);

// 괄호 적합성 판단 함수
bool IsParanBalanced(char* exp, int len) {
	Stack stack;
	InitStack(&stack);	// Make a stack empty.
	for (int i = 0; i < len; i++) {
		if (exp[i] == '(') {		// Check open symbol
			Push(&stack, exp[i]);
		}
		else if (exp[i] == ')') {	// Check close symbol
			if (IsEmpty(&stack))
				return false;	// Unbalanced case
			else
				Pop(&stack);
		}
	}
	if (IsEmpty(&stack))
		return true;	// Balanced case
	else
		return false;	// Unbalanced case
}

int main() {
	char exp[50];
	scanf("%s", exp);	// 괄호 입력

	if (IsParanBalanced(exp, strlen(exp))) {	// 괄호 문자열 적합성이 맞으면 Yes 출력
		printf("Yes");
	}
	else {		// 괄호 문자열 적합성이 틀리면 No 출력
		printf("No");
	}

	return 0;
}

// Make stack empty.
void InitStack(Stack* pstack)
{
	pstack->top = -1;
}

// Check whether stack is full.
bool IsFull(Stack* pstack) {
	return pstack->top == MAX_STACK - 1;
}

// Check whether stack is empty.
bool IsEmpty(Stack* pstack) {
	return pstack->top == -1;
}

// Read the item at the top.
Data Peek(Stack* pstack) {
	if (IsEmpty(pstack))
		exit(1);	// error: empty stack
	return pstack->items[pstack->top];
}

// Insert an item at the top.
void Push(Stack* pstack, Data item) {
	if (IsFull(pstack))
		exit(1);	// error: stack full
	pstack->items[++(pstack->top)] = item;
}

// Remove the item at the top.
void Pop(Stack* pstack) {
	if (IsEmpty(pstack))
		exit(1);	// error: empty stack
	--(pstack->top);
}