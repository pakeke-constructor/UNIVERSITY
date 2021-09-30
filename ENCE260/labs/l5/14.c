
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


typedef struct Button_t {
    u16 x;
    u16 y;
    u16 width;
    u16 height;
    void (*callback) (void);
} Button_t;


Button_t button_init(u16 x, u16 y, u16 width, u16 height, void (*callback)(void))
{
    Button_t butto;
    butto.x = x;
    butto.y = y;
    butto.width = width;
    butto.height = height;
    butto.callback = callback;

    return butto;
}


void button_click(Button_t* button)
{
    button->callback();
}




void clickFunc(void)
{
    puts("Button Clicked!");
}


int main(){
    Button_t button = button_init(480, 320, 64, 32, &clickFunc);
    button_click(&button);
}





