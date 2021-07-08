#include <stdio.h>

/* copy input to output */
void main()
{
    int c;

    while ((c = getchar()) != EOF)
        putchar(c);
}

