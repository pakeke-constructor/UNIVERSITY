



#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>
#include <stddef.h>


typedef enum Heading_t {
    NORTH,
    EAST,
    SOUTH,
    WEST
} Heading_t;


int main()
{
    Heading_t dir = NORTH;
printf("%d\n", dir == NORTH);
    return 0;
}


