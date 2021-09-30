

#include <stdio.h>
#include <stdint.h>
#include <stddef.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

#define u32 uint32_t
#define u16 uint16_t
#define u8  uint8_t

#define i32 int32_t
#define i16 int16_t
#define i8  int8_t




int main(int argc, char** argv)
{
    for (int i=0; i<argc; i++) {
        printf("[%d] %s\n", i, argv[i]);
    }
}

