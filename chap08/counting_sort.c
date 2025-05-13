#include <stdio.h>
void count_sort(int *A, int n, int k) {
  int c[k + 1];
  for (int i = 0; i < k; i++) { /* inicializa C com 0*/
    c[i] = 0;
  }
  for (int i = 0; i < n; i++) {
    c[A[i]] = c[A[i]] + 1;
  }

  int count = 0;
  for (int i = 0; i < k + 1; i++) {
    if (c[i]) {
      A[count++] = i;
    }
  }
}

int main() {
  int a[] = {1, 2, 5, 23, 20, 30, 10, 12};
  count_sort(a, 8, 50);

  for (int i = 0; i < 8; i++) {
    printf("%d ", a[i]);
  }
}
