#include<stdio.h>
#include<conio.h>
#include<string.h>

//Defining a Const which can be used throughout the program
#define MAX 25

void generateLine(int v)
{
    for(int a=0; a<MAX; a++)
    {
        if(a==25)
        {
            break;
        }
        else
        {
            // printf("\nN : %d -", a);
            putchar('-');
        }
    }
}

int main()
{
    generateLine(30);
    return 0;
}