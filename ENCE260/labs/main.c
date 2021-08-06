

#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>
#include <stddef.h>


typedef struct {
    int32_t x;
    int32_t y;
} Vec_t;


Vec_t vecSum(Vec_t v1, Vec_t v2)
{
    return (Vec_t){v1.x + v2.x, v1.y + v2.y};
}




int main(){

}




