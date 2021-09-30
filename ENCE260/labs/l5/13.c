



#include <stdio.h>
#include <stdint.h>
#include <stddef.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

#define u32 uint32_t
#define u16 uint16_t
#define u8  uint8_t

#define i32 int32_t
#define i16 int16_t
#define i8  int8_t


typedef struct Meas_s Meas_t;

struct Meas_s {
    double value;
    void (*dispFunc)(const Meas_t*);
};

void meas_print(const Meas_t* meas)
{
    meas->dispFunc(meas);
}



void disp(const Meas_t* meas)
{
    printf("%.3f m/s\n", meas->value);
}

int main(){

Meas_t meas = {2.7777, &disp};
meas_print(&meas);

}


