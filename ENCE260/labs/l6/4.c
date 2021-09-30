
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

void fillRamp(int16_t* data, size_t n)
{
    for (u32 i=0; i<n; i++) {
        data[i] = i + 1;
    }
}


int main(){
    int16_t* data = calloc(4, sizeof(int16_t));
fillRamp(data, 4);
for (size_t i = 0; i < 4; i++) {
    printf("data[%d] = %d\n", (int)i, data[i]);
}
free(data);
}
