#include <stdlib.h>
#include <stdio.h>

void selection_sort(int *a, int n){
    for (int i = 0; i < n - 1; i++)
    {
        int key = a[i];
        int min = i;

        for (int j = i + 1; j < n; j++)
        {
            if (a[j] < a[min]){
                min = j;
            }
        }

        a[i] = a[min];
        a[min] = key;
    }
    
}

int main(int argc, char const *argv[])
{
    int a[] = {3,2,4,1,5,7};
    int n = sizeof(a) / 4;
    selection_sort(a, n);

    for (int i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    

    return 0;
}
