


#include <stdio.h>
#include <ctype.h>



void printchar(char chr)
{
    if ((char)chr == '\n') {
        printf("'\\n'\n");
        return;
    }
    if ('0' <= chr && chr <= '9') {
        printf("'%c': Digit %c\n", (char)chr, (char)chr);
        return;
    }
    if ('A' <= chr && chr <= 'Z') {
        printf("'%c': Letter %d\n", (char)chr, (int)chr - 'A' + 1);
        return;
    }
    if ('a' <= chr && chr <= 'z') {
        printf("'%c': Letter %d\n", (char)chr, (int)chr - 'a' + 1);
        return;
    } else {
        printf("'%c': Non-alphanumeric\n", (char)chr);
    }
}

int main()
{
    int chr;
    while ((chr = getchar()) != EOF) {
        printchar(chr);
    }
}



