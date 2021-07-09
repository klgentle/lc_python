#include <stdio.h> 
#include <ctype.h> 
#include <math.h>

/* atof: convert string s to double */
double atof(char s[])
{
    double val, power;
    int i, sign; 

    for(i = 0; isspace(s[i]); i++)
        ;

    if (s[i] == '-') {
        sign = -1;
        i ++ ;
    }
    else if (s[i] == '+') {
        sign = 1;
        i ++ ;
    }

    for (val = 0.0; isdigit(s[i]); i++)
        val = val * 10.0 + (s[i] - '0');

    if (s[i] == '.')
        i ++ ;

    for (power = 1.0; isdigit(s[i]); i++) {
        val = val * 10.0 + (s[i] - '0');
        power *= 10.0;
    }
    
    int sign2;
    double power2;
    if (s[i] == 'e')
        i++;

    sign2 = (s[i] == '-') ? -1 : 1;
    
    if (s[i] == '-' || s[i] == '+')
        i++ ;

    for (power2 = 0; isdigit(s[i]); i++) {
        power2 = power2 * 10.0 + (s[i] - '0');
    }
    
    return sign * val / power * pow(10.0, sign2*power2);
}

void main() {

    printf("%8.10lf\n", atof("   +123.45e-6"));
}
