



#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>



size_t readString(char* string, size_t max)
{
    size_t i = 0;
    int c;
    while ((c = getchar()) != EOF && i < max) {
        if (c != '\n') {
            string[i] = c;
            i++;
        }
    }
    string[i] = '\0';
    return i;
}


int main(){
    size_t len=0;
char string[11];
len = readString(string, 10);
printf("Read String (%s) of length (%u)\n", string, len);
}





