/*
재귀함수 문제

정수 N이 주어지면 재귀함수를 이용하여 1부터 N까지의 합을 구하여 출력하는 프로그램
*/

#include <stdio.h>

// 팩토리얼 재귀함수
int Sum(int n) {
    if (n == 1) {
        return 1;
    }

    return Sum(n-1) + n;
}

int main() {
    int n;
    scanf("%d", &n);    // n 입력

    printf("%d", Sum(n));   // 1부터 n까지의 합을 출력
    return 0;
}