
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define auto __auto_type



#define LOOPi(arr) \
    for (int i=0; i <= arr.len; i++)

typedef struct {
    int len;
    int *arr;
} array;




array read(int num){
    array ints;
    ints.arr = malloc(num * sizeof(int));
    ints.len = num - 1;
    auto arr = ints.arr;
    
    int k = 0;
    while (scanf("%d", &arr[k]) == 1){
        k += 1;
    }

    return ints;
}


int det(int a, int b, int c)
{
    return b*b - 4*a*c;
}


int main()
{
    array arr = read(3);
    auto ar = arr.arr;
    
    int d = det(ar[0], ar[1], ar[2]);

    if (d < 0){
        printf("Roots are complex\n");
    }else{
        printf("Roots are real\n");
    }

    free(arr.arr);
}


