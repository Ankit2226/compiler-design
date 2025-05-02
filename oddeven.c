#include <stdio.h>

#define num 10  
int main() {
    #if (num%2 == 0)
        printf("even number  %d\n", num);
    #else
         printf("odd !!  %d\n", num);
    #endif 

    return 0;
}
