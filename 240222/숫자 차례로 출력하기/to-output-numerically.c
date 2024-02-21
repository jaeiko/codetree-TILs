/*
재귀함수 문제

정수 N이 주어지면 재귀함수를 2개 작성하여 첫 번째 재귀함수를 이용하여 1부터 N까지 숫자를 차례대로 출력하고, 
두 번째 재귀함수를 이용하여 N부터 1까지 차례로 출력하는 프로그램
*/

#include <stdio.h>

// 오름차순으로 출력하는 재귀함수
void PrintAscendingNum(int n) {
    if (n == 0) {
        return;
    }
    PrintAscendingNum(n-1);
    printf("%d ", n);
}

// 내림차순으로 숫자 출력하는 재귀함수
void PrintDescendingingNum(int n) {
    if (n == 0) {
        return;
    }
    printf("%d ", n);
    PrintDescendingingNum(n-1);
}

int main() {
    int n;
    scanf("%d", &n);    # n 입력

    // 함수 호출을 통한 결과값 출력
    PrintAscendingNum(n);
    printf("\n");
    PrintDescendingingNum(n);
    return 0;
}