

#include "temp.h"
#include <stdio.h>

void temp_set(Temp_t* temp, float value, Unit_t unit)
{
    temp->temp = value;
    temp->unit = unit;
}

static float fromCel(float temp)
{
    return temp + 273.15;
}

static float fromFar(float temp)
{
    return fromCel((temp - 32.0) * 5.0 / 9.0);
}


static float Cels(float keltemp)
{
    return keltemp - 273.15;
}



static float Faren(float keltemp)
{
    return (Cels(keltemp) * 9.0 / 5) + 32.0;
}


static float convert(const Temp_t *temp, Unit_t unit)
{
    if (temp->unit == unit) {
        return temp->temp;
    }
    switch (unit) {
        case KELVIN:
            if (temp->unit == CELSIUS) {
                return fromCel(temp->temp);
            } else { // Is Faren
                return fromFar(temp->temp);
            }
            break;

        case FAHRENHEIT:
            if (temp->unit == KELVIN) {
                return Faren(temp->unit);
            } else { // is celcius
                return Faren(fromCel(temp->unit));
            }
            break;

        case CELSIUS:
            if (temp->unit == KELVIN) {
                return Cels(temp->unit);
            } else { // is Faren
                return Cels(fromFar(temp->unit));
            }
            break;
        default:
            return 0.0;
            break;
    }
}


void temp_print(const Temp_t* temp, Unit_t unit)
{
    float deg = convert(temp, unit);

    switch (unit) {
        case FAHRENHEIT:
            printf("%.2f deg F\n", deg);
            break;
        case CELSIUS:
            printf("%.2f deg C\n", deg);
            break;
        case KELVIN:
            printf("%.2f K\n", deg);
            break;
    }
}


