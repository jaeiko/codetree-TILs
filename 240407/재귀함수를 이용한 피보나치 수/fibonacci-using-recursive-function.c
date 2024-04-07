// 값을 반환하는 재귀함수 문제
// 재귀함수를 이용한 피보나치 수

#include <stdio.h>

// 피보나치 수열 재귀함수(tail recursion 사용)
int rfiboTail(int n, int prev, int cur) {
    if (n == 1 || n == 2) return cur;   // n이 1이거나 2이면 현재값(cur) 1 반환
    else return rfiboTail(n-1, cur, prev + cur);    // 첫 번째 인자 : 횟수 | 두 번째 인자 : 이전값에 현재값 갱신 | 세번째 값 : 중간 계산값 전달
}

int main() {
    int n;  // 정수 n
    scanf("%d", &n);    // n 입력

    printf("%d", rfiboTail(n, 1, 1));   // n번째 피보나치 수 출력
    
    return 0;
}