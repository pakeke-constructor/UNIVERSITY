

#include <stdint.h>
#include <stdio.h>
#include <stddef.h>

void copyArray(const int32_t *src, int32_t *dest, size_t n)
{
    for (unsigned int i=0; i < n; i++) {
        dest[i] = src[i];
    }
}

int main(){
const int32_t array1[3] = {1, 2, 3};
int32_t array2[3] = {0};
copyArray(array1, array2, 3);
printf("%d\n", array2[0]);
printf("%d\n", array2[1]);
printf("%d\n", array2[2]);
}


