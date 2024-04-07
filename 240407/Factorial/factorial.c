// 값을 반환하는 재귀함수 문제
// 재귀함수를 이용하여 n!값을 구하는 프로그램

#include <stdio.h>

int F(int n) {
    if (n == 1) // n이 1이면 1 반환
        return 1;
    else    // n이 1 초과이면 n * F(n-1) 반환
        return n * F(n-1);
}

int main() {
    int n;  // 정수 n
    scanf("%d", &n);    // n 입력

    printf("%d", F(n));
    return 0;
}