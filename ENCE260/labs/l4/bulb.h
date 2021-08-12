


#ifndef BULB

#define BULB

#include <stdint.h>

typedef struct Bulb_t {
    uint32_t serial;
    uint8_t model;
} Bulb_t;



Bulb_t bulb_sellModel(uint8_t model);

void bulb_display(Bulb_t bulb);

uint64_t bulb_numSold(uint8_t model);


#endif
