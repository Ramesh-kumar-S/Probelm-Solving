#include<stdio.h>
#include "Extern.h"

extern int x;
int main()
{
    // extern int x;
    int x=36;
    printf("%d", x);
    return 0;

}