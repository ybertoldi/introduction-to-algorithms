#include "heap.h"
#include <stdio.h>

int find_parent(int i) { return (i + 1) / 2 - 1; }

int find_parent_from_gen(int i, int level, int gen) {
  int p = i;
  while (level-- > gen) {
    p = find_parent(p);
  }
  return p;
}

int find_left(int i) { return (i + 1) * 2 - 1; }

int find_right(int i) { return (i + 1) * 2; }

int is_left_child(int i) { return i == find_left(find_parent(i)); }

int is_left_to(int i, int j) {
  while (j < i) {
    j = find_left(j);
    if (j == i) {
      return 1;
    }
  }
  return 0;
}

int is_right_to(int i, int j) {
  while (j < i) {
    j = find_right(j);
    if (j == i) {
      return 1;
    }
  }
  return 0;
}

void max_heapify(heap *A, int i) {
  int largest;
  int l = find_left(i);
  int r = find_right(i);

  if (l < A->size && A->values[l] > A->values[i]) {
    largest = l;
  } else {
    largest = i;
  }

  if (r < A->size && A->values[largest] < A->values[r]) {
    largest = r;
  }

  if (largest != i) {
    int temp = A->values[i];
    A->values[i] = A->values[largest];
    A->values[largest] = temp;
    max_heapify(A, largest);
  }
}
 
void min_heapify(heap *A, int i) {
  int lowest;
  int l = find_left(i);
  int r = find_right(i);

  if (l < A->size && A->values[l] < A->values[i]) {
    lowest = l;
  } else {
    lowest = i;
  }

  if (r < A->size && A->values[lowest] > A->values[r]) {
    lowest = r;
  }

  if (lowest != i) {
    int temp = A->values[i];
    A->values[i] = A->values[lowest];
    A->values[lowest] = temp;
    max_heapify(A, lowest);
  }
}

heap build_max_heap(int arr[], int n){
  heap h;
  h.size = n;
  for (int i = 0; i < n ; i++) {
    h.values[i] = arr[i];
  }

  for (int i = n/2; i >= 0 ; i--) {
    max_heapify(&h, i);
  }
  return h;
}

heap build_min_heap(int arr[], int n){
  heap h;
  h.size = n;
  for (int i = 0; i < n ; i++) {
    h.values[i] = arr[i];
  }

  for (int i = 0 ; i <= n/2 ; i++) {
    min_heapify(&h, i);
  }
  return h;
}

void mostra_heap_aux(heap h, int i, int nivel) {
  if (h.size <= i)
    return;

  int p1, p2, is_left;
  for (int j = 0; j < nivel; j++) {
    p1 = find_parent_from_gen(i, nivel, j + 1);
    p2 = find_parent_from_gen(p1, j + 1, j);
    if (j != nivel - 1 && is_right_to(p1, p2)) {
      printf("      ");
    } else {
      printf("     |");
    }
  }
  printf("----%2d\n", h.values[i]);
  mostra_heap_aux(h, find_left(i), nivel + 1);
  mostra_heap_aux(h, find_right(i), nivel + 1);
}

void mostra_heap(heap h) { mostra_heap_aux(h, 0, 0); }
