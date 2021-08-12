


#include "lift.h"

Lift_t lift_init(uint8_t maxPassengers, int16_t startFloor)
{
    return (Lift_t) {
        startFloor, 0, maxPassengers
    };
}


void lift_onboard(Lift_t* lift, uint8_t peopleOff, uint8_t peopleOn)
{
    lift->passengers -= peopleOff;
    lift->passengers += peopleOn;
}


int16_t lift_goToFloor(Lift_t* lift, int16_t floor)
{
    if (lift->passengers > lift->maxPassengers) {
        return lift->floor;
    } else {
        return lift->floor = floor;
    }
}




