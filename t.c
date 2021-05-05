


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
    int x = 0;
    {
        int y = 10;
        printf("y: %d\n",y);
    }
    printf("y: %d\n",y);
    return 0;
}

