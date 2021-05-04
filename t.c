


void *add(void *ptr){
    static void *arr[10];
    static int i;
    arr[i%10] = ptr;
    return arr[i++];
}


typedef struct {
    int beans;
    char* x;
} B;


#include <stdio.h>
#include <stdlib.h>

int main(){
    B* b = (B*)malloc(sizeof b);

    printf("ptr: %d\n", (int)add(b));

    return 0;
}

