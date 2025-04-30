#include "heap.h"

int main() {
  heap h;
  int temp_values[] = {16, 14, 9, 8, 7, 10, 3, 2, 4, 1};

  for (int i = 0; i < 10; i++) {
    h.values[i] = temp_values[i];
  }
  h.size = 10;
  mostra_heap(h);

  max_heapify(&h, 2);
  mostra_heap(h);
}
