

#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>
#include <stddef.h>


typedef struct {
    int32_t x;
    int32_t y;
    int32_t vx;
    int32_t vy;
} Particle_t;


void setVelocity(Particle_t *part, int32_t vx, int32_t vy)
{
    (*part).vx = vx;
    (*part).vy = vy;
}


void update(Particle_t *particle)
{
    (*particle).x += (*particle).vx;
    (*particle).y += (*particle).vy;
}


int main(){
    Particle_t mote = {
    .x = 0,
    .y = 1,
    .vx = 0,
    .vy = 0
};
setVelocity(&mote, 3, 4);
update(&mote);
printf("v = %d, %d\n", mote.vx, mote.vy);
printf("x = %d, y = %d\n", mote.x, mote.y);
}



