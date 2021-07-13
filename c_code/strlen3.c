#include <stdio.h>

int strlen3(char *s)
{
    char *p = s;

    while (*p != '\0')
        p++;
    return p - s;
}

void main()
{
    printf("%d\n", strlen3("werjwk"));
}
