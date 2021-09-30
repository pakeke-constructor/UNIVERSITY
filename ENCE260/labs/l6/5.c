
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


char* skipping(const char* string, size_t n)
{
    char* str = malloc(n/2 + 1);
    sze i = 0;
    for (; i<n/2; i++) {
        str[i] = string[i * 2];
    }
    str[i*2 + 1] = '\0';
    return str;
}


int main(){
    char* s = skipping("0123456789", 10);
printf("%s\n", s);
free(s);
}

