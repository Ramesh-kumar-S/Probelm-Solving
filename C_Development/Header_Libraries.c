#include <stdlib.h>
#include <stdio.h>
#include <math.h>
// #define M_PI

int main()
{
    int w;
    for (w = 0; w < 10; w++)
    {
        printf("\n%.2f\n", sin(M_PI / (w + 1)));
        /* Validating the comments within String Literal */
        printf("\nRamesh - Software Engineer - Cisco");
    }
    return 0;
}