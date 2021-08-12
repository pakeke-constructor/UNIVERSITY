

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
    return (Vec_t) {
        v1.x + v2.x, v1.y + v2.y
    };
}


typedef struct {
    Vec_t position;
    Vec_t velocity;
} Particle_t;


void setVelocity(Particle_t *part, int32_t vx, int32_t vy)
{
    (*part).velocity = (Vec_t) {
        vx, vy
    };
}


void update(Particle_t *part)
{
    (*part).position = vecSum((*part).position, part->velocity);
}




int main(){
Particle_t mote = {{0, 1}, {0, 0}};
setVelocity(&mote, 3, 4);
update(&mote);
printf("v = %d, %d\n", mote.velocity.x, mote.velocity.y);
printf("x = %d, y = %d\n", mote.position.x, mote.position.y);
}




