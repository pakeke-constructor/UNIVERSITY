
#include <stdio.h>
#include <stdint.h>
#include <stddef.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

#define u64 uint64_t
#define u32 uint32_t
#define u16 uint16_t
#define u8  uint8_t

#define i64 int64_t
#define i32 int32_t
#define i16 int16_t
#define i8  int8_t

#define sze size_t


i16* ramp(size_t n)
{
    i16 *arr = malloc(n * sizeof(i16));
    for (u32 i=0; i<n; i++) {
        arr[i] = i + 1;
    }
    return arr;
}


int main(){
    int16_t* data = ramp(5);
for (size_t i = 0; i < 5; i++) {
    printf("%d ", data[i]);
}
free(data);
}
