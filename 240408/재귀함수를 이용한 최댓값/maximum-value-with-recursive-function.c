// 값을 반환하는 재귀함수 문제
// n개의 원소 중 최댓값을 구하는 프로그램

#include <stdio.h>
#include <stdlib.h>

// Max값 찾는 함수(By Function Call for Tail Recursion)
int rfindMaxTail(int* arr, int n, int max) {
    if (n == 1) // n이 1이면 배열 순회를 다한 것이므로 최종 max값 반환
        return max;

    if (max <= arr[n - 1]) {    // 현재 max값보다 arr[n-1] 값이 크면 max값 갱신
        max = arr[n - 1];
    }
    return rfindMaxTail(arr, n - 1, max);   // 계속 arr[n-1]과 max값 비교하기(by 재귀함수)
}

int main() {
    int n;  // 정수 n
    scanf("%d", &n);    // n 입력

    int* arr = malloc(sizeof(int) * n); // 정수 4byte * n의 크기만큼 동적할당해서 heap 영역에 arr 배열 저장(그냥 int arr[n] 하면 컴파일 시점에 n이 얼마인지 모르므로 에러 발생한다.)
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);   // 각 정수를 입력받아 arr[i]에 해당하는 주소로 찾아가 저장.
    }

    printf("%d", rfindMaxTail(arr, n, arr[n-1]));    // arr의 원소들 중 최댓값 출력
    return 0;
}