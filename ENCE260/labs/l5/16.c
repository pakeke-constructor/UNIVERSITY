

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

#define i64 uint64_t
#define i32 int32_t
#define i16 int16_t
#define i8  int8_t

#define sze size_t



int comp(const void* fst, const void* snd)
{
    const u64 *fst_ = fst;
    const u64 *snd_ = snd;
    const u64 first  = *fst_;
    const u64 second = *snd_;
    if (first > second) {
        return 1;
    } else if (second > first) {
        return -1;
    } else {
        return 0;
    }
}



#define ASIZE 10



int main()
{
    u64 buf[ASIZE];
    for (int i=0; i<ASIZE; i++) {
        scanf("%lu", &buf[i]);
    }

    qsort(&buf[0], ASIZE, sizeof(unsigned int), comp);

    for (int j=0; j<ASIZE; j++) {
        printf("%lu\n", buf[j]);
    }   
}
