// 값을 반환하는 재귀함수 문제
// 3자리로 이루어진 정수 3개가 주어지면 그 세 숫자들을 곱한 후, 그 결과값의 각 자리 숫자들의 합을 구하여 출력하는 프로그램

#include <stdio.h>

int F(int n) {
    if (n < 10) {   // n이 한 자리 수면 n 리턴
        return n;
    }
    return F(n / 10) + n % 10;  // 재귀함수를 사용해 n의 첫 번째 숫자를 더하면서 연산 이어나감.
}

int main() {
    int a, b, c;    // 정수 a, b, c
    scanf("%d %d %d", &a, &b, &c);  // 정수 a, b, c 순서대로 입력
    int multiply = a * b * c;   // multiply는 a와 b, c를 곱한 값

    printf("%d", F(multiply));  // multiply의 각 자리 숫자들을 더한 값 출력
    return 0;
}