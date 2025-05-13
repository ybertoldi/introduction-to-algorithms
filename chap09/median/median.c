#include "heap.h"
#include <stdio.h>

int my_ceil(double d) {
  int rnd = (int)d;
  return ((d - rnd) > 0) ? d+1 : d;
}
int my_floor(double d) { return (int)d; }

void heapsort(int *A, int n) {
  heap h = build_max_heap(A, n);

  for (int i = n - 1; i >= 1; i--) {
    int temp = h.values[i];
    h.values[i] = h.values[0];
    h.values[0] = temp;
    h.size--;

    max_heapify(&h, 0);
  }

  for (int i = 0; i < n; i++) {
    A[i] = h.values[i];
  }
}

void mostra_array(int A[], int n) {
  for (int i = 0; i < n; i++) {
    printf("%d ", A[i]);
  }
  printf("\n");
}

int main() {
  int a[] = {1, 4, 10, 12, 2, 9, 15, 2, 24};
  int n = sizeof(a) / sizeof(a[0]);
  heapsort(a, n);
  mostra_array(a, n);

  double middle = n / 2.0;
  int lwr_med = my_ceil(middle);
  int upr_med = my_floor(middle);
  double val = (a[lwr_med] + a[upr_med]) / 2.0;

  printf("median: %f\n", val);
  return 0;
}
