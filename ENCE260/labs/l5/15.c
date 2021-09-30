


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

#define sze size_t


void processBuffer(void* buffer, size_t numElements,
            size_t elementSize, void (*processFunc)(void*))
{
    sze i = 0;
    for(; i<numElements; i++) {
        processFunc((void*)(((sze)buffer) + i * elementSize));
    } 
}


void processU64(void* element)
{
    printf("%d\n", *(int*)element);
}

int main(void)
{
    uint64_t arr[11] = {0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024};
    processBuffer((void*)arr, 11, sizeof(uint64_t), &processU64);
}

