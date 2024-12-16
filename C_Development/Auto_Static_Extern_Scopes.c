#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<time.h>

int SharedVar_A = 26; //Global Variable
typedef int ramesh;

int Google(void)
{
    printf("\nFrom Function = %d", SharedVar_A);
    return(SharedVar_A);
}

int main()
{
    time_t Now;
    // static int A;
    int A;
    A = Google();
    printf("\nMain function Return Value is %d", A);
    time(&Now);
    printf("%s", ctime(&Now));

    puts("Gonna Print the New Data Type Buddy");
    ramesh r= 34;
    printf("%d", r);

    char l = 'a';
    printf("\nType casted char is - %f", (float)l);

}
