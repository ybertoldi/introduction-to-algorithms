#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int *a1, int *a2) {
  int temp = *a1;
  *a1 = *a2;
  *a2 = temp;
}

int partition(int *A, int p, int r) {
  int piv = A[r];
  int i = p - 1, j = p;

  while (j < r) {
    if (A[j] <= piv) {
      i++;
      swap(&A[i], &A[j]);
    }
    j++;
  }

  A[r] = A[i + 1];
  A[i + 1] = piv;
  return i + 1;
}


int randomized_partition(int *A, int p, int r) {
  srand(time(0));
  int ran = (rand() % (r - p)) + p;

  int piv = A[ran];
  swap(&A[r], &A[ran]);

  int i = p - 1, j = p;
  while (j < r) {
    if (A[j] <= piv) {
      i++;
      swap(&A[i], &A[j]);
    }
    j++;
  }
  A[r] = A[i + 1];
  A[i + 1] = piv;
  return i + 1;
}


void quicksort(int *A, int p, int r) {
  if (p >= r)
    return;
  int q = partition(A, p, r);
  quicksort(A, p, q - 1);
  quicksort(A, q + 1, r);
}


int main() {
  int a[] = {3, 2, 4, 5, 1, 2, 0, 15, 14, 9, 10};
  quicksort(a, 0, 10);
  for (int i = 0; i < 11; i++) {
    printf("%d ", a[i]);
  }
  return 0;
}
