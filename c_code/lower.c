#include <stdio.h>

/* lower: convert c to lower case */

int lower(int c)
{
    if (c >= 'A' && c <= 'Z')
        return c + 'a' - 'A';
    else
        return c;
}


void main() 
{
    printf("%d\n", lower(66));
}
