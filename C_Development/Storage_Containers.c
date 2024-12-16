#include<stdio.h>
#include<stdlib.h>

int storageClass()
{
    static int count = 0;
    count++;
    return count;
}

int main()
{
    // int a;
    extern int a;
    extern int a;
    extern int a;

    puts("\nStarting to invoke the function");
    printf("\nStorage Count Value : %d", storageClass());
    printf("\nStorage Count Value : %d", storageClass());
    printf("\nStorage Count Value : %d", storageClass());
    printf("\nFinal Storage Count Value : %d", storageClass());

    return(0);
}