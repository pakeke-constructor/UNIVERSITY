

#include <stdint.h>
#include <stdio.h>



void printSquares(uint32_t n)
{
    for (int i=1; i <= (int)n; i++){
        printf("%d\n", i * i);
    }
}


int main(){
    printSquares(1);
    printSquares(4);
    return 0;
}

