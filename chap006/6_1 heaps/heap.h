typedef struct heap {
  int values[100];
  int size;
} heap;

int find_parent(int i);
int find_left(int i);
int find_right(int i);
void max_heapify(heap *A, int i);
void mostra_heap(heap h);
heap build_max_heap(int arr[], int n);
heap build_min_heap(int arr[], int n);
