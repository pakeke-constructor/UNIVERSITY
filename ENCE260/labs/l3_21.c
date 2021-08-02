
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>


void printSquaredArray(const int32_t arr[], size_t n)
{
    for (size_t i=0; i<n; i++) {
        printf("%d\n", arr[i] * arr[i]);
    }
}


int main(){
const int32_t array[3] = {1, 2, 3};
printSquaredArray(array, 3);
}

