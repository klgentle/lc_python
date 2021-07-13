#include <stdio.h>


#define forever for(;;)  /* infinite loop */
#define max(A, B) ((A) > (B) ? (A) : (B)) 
//#define paste(front, back)  front ## back

/*
#if SYSTEM == SYSV
    //#define HDR "sysv.h"
    ;
#elif SYSTEM == BSD
    #define HDR "bsd.h"
#elif SYSTEM == MSDOS
    #define HDR "msdos.h"
#else
    #define HDR "default.h"
#endif
#include HDR
*/

void main() {
    //printf("paste(name, 1):%s", paste("name", "1"));
    //printf("HDR:%s", HDR);
    printf("hello, world\n");
}
