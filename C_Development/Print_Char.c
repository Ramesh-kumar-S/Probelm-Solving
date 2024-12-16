#include<stdio.h>
#include<conio.h>
int main()
{
    char string[] = "Ramesh - Passionate Software Engineer\n";
    int index = 0;
    while(string[index] != '\0')
    {
        putchar(string[index]);
        putchar('\n');
        index++;
    }
    return 0;
}