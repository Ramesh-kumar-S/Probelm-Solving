/* PreProcessor Directives*/
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define COUNT 10
#define STATEMENT "Ramesh - Most Stubborn and Positive Person"
/*Main Function*/
int main()
{
    int a,b;
    /*Fetching the Input*/
    printf("Enter the Positive Number : ");
    b=COUNT;
    // scanf("%d", &b);
    for(a=0; a<b; a++)
    {
        printf("%s\n",STATEMENT);
        if(a==9)
        {
            break;
        }
    }
}
