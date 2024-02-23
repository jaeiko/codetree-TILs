/*
재귀함수 문제

N이 주어지면 재귀함수를 단 하나만 이용하여 다음과 같이 출력하는 프로그램
*/

#include <stdio.h>

void PrintNum(int n) {
    if (n == 0) {
        return;
    }
    printf("%d ", n);   // N에서 1까지 1씩 감소하며 하나씩 출력
    PrintNum(n-1);
    printf("%d ", n);   // 재귀함수 호출 끝난 후 다시 1부터 N까지 1씩 증가하며 출력
}

int main() {
    int n;
    scanf("%d", &n);    // n 입력
    PrintNum(n);
    return 0;
}