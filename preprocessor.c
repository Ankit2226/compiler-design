#include <stdio.h>

#define Year 2025  
int main() {
    #if (Year == 2025)
        printf("This Year: %d\n", Year);
    #elif (Year > 2025)  
        printf("Upcoming Year: %d\n", Year);
    #elif (Year < 2025) 
        printf("Previous Year: %d\n", Year);
    #else
        printf("Invalid Year: %d\n", Year);
    #endif 

    return 0;
}
