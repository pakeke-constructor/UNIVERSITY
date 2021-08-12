

#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>
#include <stddef.h>


typedef enum {
    January,
    February,
    March,
    April,
    May,
    June,
    July,
    August,
    September,
    October,
    November,
    December
} Month_t;


typedef struct Date_t {
    uint16_t year;
    Month_t month;
    uint8_t day;
} Date_t;



Date_t setDate(uint8_t day, uint8_t month, uint16_t year)
{
    return (Date_t) {
        year, (Month_t)month, day
    };
}


void printDate(const Date_t* date)
{
    static const char *months[] = {
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    };

    printf("%d %s %d\n", date->day, months[(int)date->month - 1], date->year);
}

int main(){Date_t date = setDate(20, 7, 1969);
printDate(&date);}