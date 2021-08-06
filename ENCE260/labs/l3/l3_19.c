
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>





int main(){
    int32_t buffer[100];
    int32_t val;
    int i = 0;

    while (i < 100) {
        scanf("%d\n", &val);
        if (val == -1) {
            break;
        }

        buffer[i] = val;
        i++;
    }

    printf("%d numbers entered\n", i);

    for (int u = 0; u < i; u++) {
        printf("%d\n", buffer[u]);
    }
}

