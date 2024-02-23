/*
재귀함수 문제

1번째 N번째 줄까지 별 출력을 다음 모양으로 재귀함수를 이용해 출력하는 프로그램
*/

#include <stdio.h>

// 별을 탑 쌓듯이 출력해주는 재귀함수
void PrintStar(int n) {
    if (n == 0) {
        return;
    }
    PrintStar(n-1);
    for (int i = 0; i < n; i++){
        printf("*");
    }
    printf("\n");
}

int main() {
    int n;
    scanf("%d", &n);    // n 입력
    PrintStar(n);
    return 0;
}