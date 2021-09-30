
#include <stdio.h>
#include <stdint.h>
#include <stddef.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define u64 uint64_t
#define u32 uint32_t
#define u16 uint16_t
#define u8  uint8_t

#define i64 int64_t
#define i32 int32_t
#define i16 int16_t
#define i8  int8_t

#define sze size_t




typedef struct {
    bool isNegative;
    u16 magnitude;
} SignMag_t;


SignMag_t signMag_init(bool isneg, u16 mag)
{
    return (SignMag_t) {
        isneg,
        mag
    };
}

void signMag_print(SignMag_t value)
{
    if (value.isNegative) {
        printf("-");
    } else {
        printf("+");
    }

    printf("%d\n", value.magnitude);
}


SignMag_t signMag_read(void)
{
    bool isneg = false;
    
    u16 numbers[1000];
    u16 len = 0;

    int c;
    c = getchar();
    if (c == '+') {
        isneg = false;
    } else if (c == '-') {
        isneg = true;
    } else if (isdigit(c)) {
        numbers[len] = c - '0';
        len++;
    } else {
        return signMag_init(true, 0);
    }

    c = getchar();
    while (isdigit(c)) {
        numbers[len] = c - '0';
        len++;
        c = getchar();
    }

    u64 ans = 0;
    for (int i=0; i<=len; i++) {
        ans += (numbers[i] * pow(10, len - i));
    }

    u16 max = (u16)-1;

    if (ans > (u64)max) {
        ans = max;
    }

    printf("maxx:: %d\n", (i32) max);

    return signMag_init(isneg, ans);
}


int main()
{
    signMag_read();
}
