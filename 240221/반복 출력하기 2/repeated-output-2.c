/*
재귀함수 문제

정수 N이 주어지면 재귀함수를 이용해서 문자열 "HelloWorld"를 N번 출력하는 프로그램
*/

#include <stdio.h>

void PrintHelloWorld(int n) {    // 1부터 n번째 줄까지 HelloWorld를 출력하는 함수
    if(n == 0){             // n이 0이라면, 더 이상 진행하지 않고
        return;             // 퇴각한다.
    }

    PrintHelloWorld(n - 1);       // 1부터 n - 1번째 줄까지 출력하는 함수
    printf("HelloWorld\n");
}

int main() {
    int n;
    scanf("%d", &n);
    PrintHelloWorld(n);
    return 0;
}