#include <stdlib.h>
#include <stdio.h>
#include <time.h>

long long fastExp(long long a,long long b){
    if (b == 0){
        return 1;
    } else if (b % 2 == 0)
    {
        long long temp = fastExp(a, b / 2);
        return temp * temp;
    } else {
        return  a * fastExp(a, b - 1);
    }
    
}

long long naiveExp(long long a,long long b){
    long long val = a;
    for (int i = 0; i < b; i++)
    {
        val *= a;
    }

    return val;
    
}

int main(int argc, char const *argv[])
{
    clock_t start, end;

    start = clock();
    for (long i = 1; i < 100000; i++)
    {
        fastExp(i, i + (int) (0.25 * i));
    }
    
    end = clock();
    printf("%f \n", (((double) (end - start)) / CLOCKS_PER_SEC));


    
    start = clock();
    for (long i = 1; i < 100000; i++)
    {
        naiveExp(i, i + (int) (0.25 * i));
    }
    end = clock();
    printf("%f \n", (((double) (end - start)) / CLOCKS_PER_SEC));

    return 0;
}
