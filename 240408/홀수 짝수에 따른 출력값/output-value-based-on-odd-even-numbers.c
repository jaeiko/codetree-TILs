// 값을 반환하는 재귀함수 문제
// 정수 N이 주어지고, N이 홀수인 경우에는 1부터 N까지의 홀수를, 
// N이 짝수인 경우에는 2부터 N까지의 짝수의 합을 출력하는 프로그램을 재귀 함수를 이용하기
#include <stdio.h>

int F(int n, int sum) {
    if (n == 1 || n == 2)   // n이 1이거나 2인 인 경우 최종 결과값인 sum + n 반환
        return sum + n;

    return F(n-2, sum + n); // 인자 n-2와 중간 계산값인 sum + n을 함수 F에 전달하여 재귀함수 호출
}

int main() {
    int n;  // 정수 n

    scanf("%d", &n);    // n 입력
    printf("%d", F(n, 0));  // N이 홀수인 경우에는 1부터 N까지의 홀수를, N이 짝수인 경우에는 2부터 N까지의 짝수의 합을 출력

    return 0;
}