// 값을 반환하는 재귀함수 문제
// 첫 번째는 2, 두 번째는 4, 세 번째부터는 앞의 두 수의 곱을 100으로 나눈 나머지로 이루어진 수열이 있다. 
// 100 이하의 정수 N을 입력받아 재귀함수를 이용하여 N번째 값을 구하여 출력하는 프로그램
#include <stdio.h>

int recursion(int n, int prev, int cur) {
    if (n == 1) return 1;   // n이 1일 때 최종값 2 반환(첫 번째 값에 해당)
    if (n == 2) return 2;   // n이 2일 때 최종 연산값 4 반환(두 번째 값에 해당)
    if (n == 3) return (prev * cur) % 100; // n은 3일 때 최종 연산 값인 cur값 반환

    return recursion(n - 1, cur, (prev * cur) % 100); // 이전값에 현재값으로 갱신하고, 현재값을 중간 계산 값으로 갱신하여 인덱스 - 1값과 함께 인자로 전달
}

int main() {
    int n;  // 정수 n
    scanf("%d", &n);    // n 입력

    printf("%d", recursion(n, 2, 4));   // n, 첫 번째 값 2, 두 번째 값 4를 recursion 함수에 전달하여 수열의 n번째 값 출력
    return 0;
}