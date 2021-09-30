
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

typedef struct {
    char random;
    int8_t junk;
} Data_t;


Data_t *newData(char random, i8 junk)
{
    Data_t *data = malloc(sizeof(Data_t));
    data->random = random;
    data->junk = junk;
    return data;
}


void freeData(Data_t *data)
{
    free(data);
}

int main(){
Data_t* data = newData('A', 1);
printf("%c %d\n", data->random, data->junk);
freeData(data);

}
