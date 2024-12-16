#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int a;
    float b;
    char c[100];
    double d;

    printf("Please enter the ID : ");
    scanf("%d", &a);

    printf("Experience Level : ");
    scanf("%f", &b);

    // Clear the input buffer
    while ((getchar()) != '\n')
        ;

    printf("Role & Company: ");
    fgets(c, sizeof(c), stdin);

    // Remove the trailing newline character from the string
    size_t len = strlen(c);
    if (len > 0 && c[len - 1] == '\n')
    {
        c[len - 1] = '\0';
    }

    printf("CTC : ");
    scanf("%lf", &d);

    puts("------------------------------------");
    printf("\nID : %d\n", a);
    printf("Experience level : %.2f\n", b);
    printf("Role & Org : %s\n", c);
    printf("CTC : %.2f\n", d);
    puts("------------------------------------");

        return 0;
}