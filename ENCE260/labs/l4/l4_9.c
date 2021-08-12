





#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>
#include <stddef.h>



typedef enum Gear_t {
    REVERSE = -1,
    NEUTRAL = 0,
    FIRST = 1,
    SECOND,
    THIRD,
    FOURTH,
    FIFTH
} Gear_t;




int main()
{
    Gear_t currentGear = FIRST;
printf("%d\n", currentGear + THIRD);
}


