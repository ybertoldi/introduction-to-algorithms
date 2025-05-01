#include "heap.h"
#include <stdio.h>

void heapsort(int A[], int n) {
  heap h = build_max_heap(A, n);

  mostra_heap(h);
  for (int i = n - 1; i >= 1; i--) {
    printf("-----------------passo %d----------------\n", n - i);
    mostra_heap(h);
    printf("\n\n");

    int temp = h.values[i];
    h.values[i] = h.values[0];
    h.values[0] = temp;
    h.size--;

    printf("apos a troca:\n");
    mostra_heap(h);
    printf("\n\n");

    max_heapify(&h, 0);

    printf("apos o heapify\n");
    mostra_heap(h);
    printf("\n\n");

    printf("array:  ");
    for (int i = h.size; i < n; i++) {
      printf("%d ", h.values[i]);
    }
    printf("\n");
  }

  printf("array final:  ");
  for (int i = 0; i < n; i++) {
    printf("%d ", h.values[i]);
  }
  printf("\n");
}

int main() {
  int a[] = {1, 4, 10, 12, 2, 9, 15, 2, 24};
  heapsort(a, 9);

  return 0;
}
