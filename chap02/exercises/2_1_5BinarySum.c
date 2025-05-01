#include <stdio.h>
#include <stdlib.h>

int maxVal(int a, int b){
    if (a >= b){
        return a;
    }
    return b;
}

int* sumBinary(int *a, int *b, int n){
    int *c = (int *)malloc( (n) * sizeof(int) );
    int carry = 0;

    for (int i = n - 1; i > 0; i--)
    {
        c[i] = (a[i - 1] + b[i - 1] + carry) % 2;

        if (a[i - 1] + b[i - 1] + carry >= 2){
            carry = 1;
        }
        else{
            carry = 0;
        }
    }

    c[0] = carry;
    return c;
}

int main(int argc, char const *argv[])
{
    int a[] = {0, 1, 0, 0, 1, 1}; // 19
    int b[] = {1, 0, 0, 0, 1, 1}; // 35
    int n = maxVal(sizeof(a) / 4, sizeof(b) / 4) + 1;
    int *c = sumBinary(a, b, n);

    for (int i = 0; i < n; i++)
    {
        printf("%d ", c[i]);
    }
    free(c);

    return 0;
}
