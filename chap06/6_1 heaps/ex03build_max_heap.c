#include "heap.h"

int main() {
  int a[] = {1, 4, 10, 12, 2, 9, 15, 2, 24};
  heap h = build_max_heap(a, 9);
  mostra_heap(h);

  heap h2 = build_min_heap(a, 9);
  mostra_heap(h2);
  return 0;

}
