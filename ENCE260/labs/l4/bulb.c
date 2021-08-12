

#include <stdio.h>

#include "bulb.h"


static uint64_t sales[256] = {0};


Bulb_t bulb_sellModel(uint8_t model)
{
    uint64_t sale = sales[model];
    sales[model] += 1;
    return (Bulb_t) {
        sale, model
    };
};

void bulb_display(Bulb_t bulb)
{
    printf("Model %d, SN%06d\n", bulb.model, bulb.serial);
};

uint64_t bulb_numSold(uint8_t model)
{
    return sales[model];
}





