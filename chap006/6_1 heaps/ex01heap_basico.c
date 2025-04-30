// ver figura 6.1
#include "heap.h"
#include <stdio.h>
int main() {
  heap h;
  int temp_values[] = {16, 14, 10, 8, 7, 9, 3, 2, 4, 1};

  for (int i = 0; i < 10; i++) {
    h.values[i] = temp_values[i];
  }
  h.size = 10;

  for (int i = 0; i < 4; i++) {
    printf("os filhos de %d sao %d e %d \n", h.values[i],
           h.values[find_left(i)], h.values[find_right(i)]);
  }

  for (int i = 0; i < 10; i++) {
    printf("o pai de %d eh %d\n", h.values[i], h.values[find_parent(i)]);
  }
}
