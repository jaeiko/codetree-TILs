/*
재귀함수 문제

정수 n의 값을 입력받아 별 출력을 다음 모양으로 재귀함수를 이용해 출력하는 프로그램
*/

#include <stdio.h>

// 별 내림차순 출력 재귀함수
void PrintDescendingStar(int n) {
    if (n == 0) {
        return;
    }
    for(int i = 0; i < n; i++) {
        printf("* ");
    }
    printf("\n");
    PrintDescendingStar(n-1);
}

// 별 오름차순 출력 재귀함수
void PrintAscendingStar(int n) {
    if (n == 0) {
        return;
    }
    PrintAscendingStar(n-1);
    for(int i = 0; i < n; i++) {
        printf("* ");
    }
    printf("\n");
}

int main() {
    int n;
    scanf("%d", &n);    // 정수 n 입력
    PrintDescendingStar(n); // 별 내림차순으로 출력
    PrintAscendingStar(n);  // 별 오름차순으로 출력
    return 0;
}