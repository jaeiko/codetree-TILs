#include <stdio.h>
#include <stdlib.h>

int recursion(int* arr, int index, int search) {
    if (index == 1 || index == 2) return index; // 찾고자 하는 index의 값이 1이거나 2이면 index(1 또는 2) 반환

    arr[index] = arr[index / 3] + arr[index - 1];   // N 번째 수는 (N/3)번째 수와 (N-1)번째 수의 합으로 나열된 수열
    if (index == search) return arr[index]; // 우리가 찾고자 하는 값에 해당하는 인덱스에 도달했다면 해당 요소 반환
    return recursion(arr, index + 1, search);   // 못 찾았으면 index값에 1을 더해 다시 재귀함수 호출
}

int main() {
    int n;  // 정수 n
    scanf("%d", &n);    // n 입력
    int* arr = malloc(sizeof(int) * (n+1));  // 4byte * n 크기의 동적배열 할당

    // 배열의 첫 번째 요소와 두 번째 요소는 각각 1, 2
    arr[0] = 0;
    arr[1] = 1;
    arr[2] = 2;

    printf("%d", recursion(arr, 3, n));  // 인자값으로 배열 arr과 n, n-1(=search:우리가 찾고자 하는 값의 인덱스), 2(배열의 세번째 수에 해당하는 인덱스) 전달해서 계산 후 n번째 수를 출력
    return 0;
}