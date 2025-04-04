#include <stdio.h>
#include <stdlib.h>

void merge(int A[], int l, int m, int r)
{
    int n1 = m - l + 1;
    int n2 = r - m;

    int L[n1], R[n2];

    for (int i = 0; i < n1; i++)
        L[i] = A[l + i];

    for (int j = 0; j < n2; j++)
        R[j] = A[m + 1 + j];

    int i = 0;
    int j = 0;
    int k = l;
    
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j]){
            A[k] = L[i];
            i++;
        }
        else{
            A[k] = R[j];
            j++;
        }

        k++;
    }

    while (i < n1){
        A[k] = L[i];
        i++;
        k++;
    }

    while (j < n2)
    {
        A[k] = R[j];
        j++;
        k++;
    }
    

}

void mergeSort(int A[], int l, int r)
{
    if (l >= r){
        return;
    }

    int m = (l + r) / 2;
    mergeSort(A, l, m);
    mergeSort(A, m+1, r);
    merge(A, l, m, r);

}

// int main(int argc, char const *argv[])
// {
//     // testando a função merge
//     // int A[] = {1,4,6,7,1,2,3,5};
//     // merge(A, 0, 3, 7);

//     int A[] = {1,0,2,7,1,3,2,5};
//     int size = sizeof(A) / sizeof(A[0]);
//     mergeSort(A, 0, size - 1);
    
//     for (int i = 0; i < size; i++)
//     {
//         printf("%d ", A[i]);
//     }

//     return 0;
// }
