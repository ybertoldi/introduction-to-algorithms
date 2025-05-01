#include "max_heap.h"
#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
  int a[] = {1, 4, 10, 12, 2, 9, 15, 2, 24};
  heap H = build_max_heap(a, 9);
  mostra_heap(H);
  
  srand(time(0));

  for (int i = 0; i < 15; i++) {
    int r = rand() % 100;
    max_heap_insert(&H, r);
    printf("inserindo %d\n", r);
    mostra_heap(H);
    printf("\n");
  }

  for (int i = 0; i < 5; i++) {
    printf("tirando o primeiro item\n");
    max_heap_pop(&H);
    mostra_heap(H);
    printf("\n");
  }
}
