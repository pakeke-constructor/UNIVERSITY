

#include <stdio.h>


int multiply(int a, int b){return a*b;}



int (*mulFunc)(int, int) = &multiply;




int main(){
    printf("MULS: %d\n", mulFunc(34, 56));
}
