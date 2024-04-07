// 값을 반환하는 재귀함수 문제
// N이 짝수이면 2로 나누고, 홀수이면 3으로 나눈 몫을 취하는 작업을 반복하다가 
// 그 값이 1이 되면 그때까지 진행한 작업의 횟수를 구하는 프로그램을 재귀 함수를 이용하여 작성

#include <stdio.h>

int F(int n, int count) {
    if (n == 1)     // n이 1이면 count값 리턴
        return count;   

    if (n % 2 == 0)
    {
        return F(n/2, count + 1);   // n이 짝수이면 n/2, count+1 값을 재귀함수 F에 전달해서 다시 호출
    }
    else
    {
        return F(n/3, count + 1);   // n이 홀수이면 n/3, count+1 값을 재귀함수 F에 전달해서 다시 호출
    }
}

int main() {
    int n;  // 정수 : n
    int count = 0;  // 진행한 작업의 횟수 : count
    scanf("%d", &n);

    printf("%d", F(n, count));  // 나누는 작업의 횟수 출력
    return 0;
}