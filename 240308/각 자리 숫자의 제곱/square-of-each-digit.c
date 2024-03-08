/*
재귀함수 문제
8자리 이하의 정수 N이 주어지면 재귀함수를 이용하여 각 자리 숫자의 제곱의 합을 출력하는 프로그램
*/

#include <stdio.h>

// 각 자리 숫자의 제곱의 합을 구하는 재귀함수
int F(int n) {
    if(n < 10) {
        return n * n;
    }

    return F(n / 10) + ((n % 10) * (n % 10));
}

int main() {
    int n;
    scanf("%d", &n);    // n 입력

    printf("%d", F(n)); // F(n) 결과 출력

    return 0;
}