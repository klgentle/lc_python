#include <stdio.h>

void main() {
    int x = 1, y = 2, z[10]={7,1,2,6,3,4};
    int *ip;        /* ip is a pointer to int */
    
    ip = &x;        /* ip is not points to x */
    y = *ip;        /* y is now 1 */
    *ip = 0;        /* x is not 0 */
    ip = &z[0];     /* ip now points to z[0] */

    printf("ip:%d\n", *ip);
}
