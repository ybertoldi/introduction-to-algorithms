#include <stdio.h>
#include <stdlib.h>
#include "../mergesort.h"

int contains(int a[], int n, int target){
    mergeSort(a, 0, n-1);
    int i = 0;
    int j = n -1;

    while (i < j)
    {
        if (a[i] + a[j] == target){
            printf("(%d, %d) -> ", a[i], a[j]);
            return 1;
        }
        if (a[i] + a[j] > target){
            j--;
        }
        if (a[i] + a[j] < target){
            i++;
        }
    }

    return 0;
}

int main(int argc, char const *argv[])
{
    int a[] = {2,1,7,6,5,8,2,3,10};
    for (int i = 0; i < 21; i++)
    {
        if (contains(a, 9, i)){
            printf("contains %d\n", i);
        }
    }

    return 0;
}
