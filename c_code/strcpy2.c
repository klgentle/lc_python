#include <stdio.h>

/* strcpy2: copy t to s */
void strcpy2(char *s, char *t)
{
    while (*s++ = *t++)
        ;
}

void main()
{
    char *t = "smile"; 
    char *s;
    printf("t:%s\n", t);
    strcpy2(s, t);
    printf("s:%s\n", s);  // Segmentation fault (core dumped)
}
