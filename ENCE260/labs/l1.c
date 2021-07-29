

#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>
#include <math.h>


float det(float a, float b, float c)
{
    return (b * b - 4 * a * c);
}

void printRoots(float a, float b, float c)
{
    if (a == 0) {
        printf("Not a quadratic\n");
        return;
    }
    if (det(a, b, c) < 0) {
        printf("Imaginary roots\n");
        return;
    }

    double root1 = (-b + sqrt(b * b - 4 * a * c)) / (2*a);
    double root2 = (-b - sqrt(b * b - 4 * a * c)) / (2*a);
    if (root1 > root2) {
        printf("Roots are %.4f and %.4f\n", root2, root1);
    } else {
        printf("Roots are %.4f and %.4f\n", root1, root2);
    }
}

int main(){
printRoots(1, -4, 3);
printRoots(1, 2, 3);
printRoots(0, 2, 3);
printRoots(1, 0, -1);
    return 0;
}

