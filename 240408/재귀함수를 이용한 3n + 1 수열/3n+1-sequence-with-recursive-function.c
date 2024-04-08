// 값을 반환하는 재귀함수
// 자연수 n에서 시작하여 n이 짝수면 2로 나누고, n이 홀수면 3을 곱하고 1을 더하는 것을 n이 1이 되기 전까지 계속 반복하려고 할 때,
// 총 몇 번을 반복해야 1이 되는지를 계산하는 프로그램

#include <stdio.h>

int recursion(int n, int count) {
    if (n == 1) return count;   // n 이 1이면 최종 연산 횟수 반환
    if (n % 2 == 0) {   // n이 짝수이면 인자로 n을 2로 나눈 값과 count + 1 값을 recursion 함수에 전달하여 재귀함수 호출
        return recursion(n / 2, count + 1);
    } else {    // n이 홀수이면 인자로 n에 3을 곱하고 1을 더한 값과 count + 1 값을 recursion 함수에 전달하여 재귀함수 호출
        return recursion(n * 3 + 1, count + 1);
    }
}

int main() {
    int n;  // 정수 n
    scanf("%d", &n); // 정수 n 입력

    printf("%d", recursion(n, 0));  // 재귀함수를 이용해 연산 횟수 count 값을 출력
    return 0;
}