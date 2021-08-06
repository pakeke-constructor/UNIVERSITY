
#include <stdbool.h>
#include <stdint.h>
#include <stddef.h>
#include <stdio.h>


bool isInData(const uint8_t* data, size_t arraySize,
                const uint8_t* ptr)
{
    return (data <= ptr) && (ptr <= data + arraySize - sizeof(uint8_t));
}

int main(){
    const uint8_t x;
const uint8_t thing[3];
const uint8_t y;
printf("%d\n", isInData(thing, 3, &x));
printf("%d\n", isInData(thing, 3, &thing[0]));
printf("%d\n", isInData(thing, 3, &thing[1]));
printf("%d\n", isInData(thing, 3, &thing[2]));
printf("%d\n", isInData(thing, 3, &thing[3]));
printf("%d\n", isInData(thing, 3, &y));
}