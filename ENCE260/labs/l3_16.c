

#include <stddef.h>
#include <stdint.h>
#include <stdio.h>


void printArray(int32_t* arr, size_t n)
{
    for (size_t i=0; i<n; i++){
        printf("%d\n", *arr);
        arr += 1;
    }
}

int main(){
    int32_t array[3] = {1, 2, 3};
printArray(array, 3);
}
