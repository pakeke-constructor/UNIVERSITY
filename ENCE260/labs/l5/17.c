


#include <stdio.h>
#include <stdint.h>
#include <stddef.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

#define u32 uint32_t
#define u16 uint16_t
#define u8  uint8_t

#define i32 int32_t
#define i16 int16_t
#define i8  int8_t

#define sze size_t


typedef int32_t* (*Func_t)(int32_t*, size_t);


int32_t* offsetArray(int32_t* array, size_t offset){
    return array + offset;
}

int main(void)
{
    Func_t func = &offsetArray;
    
    int32_t arr[5] = {1, 2, 3, 4, 5};
    int32_t* offsetArr = (*func)(arr, 2);
    printf("%d\n", (int)(offsetArr - arr));
}

