#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int j, temp, n, i;
    scanf("%d", &n);
    temp = n;
    for (i = 0; i < n; i++) {
        for (j = 0; j < i; j++) {
            printf("%d ", n - j);
        }
        for (j = 0; j < 2 * temp - 1; j++) {
            printf("%d ", temp);
        }
        for (j = i - 1; j >= 0; j--) {
            printf("%d ", n - j);
        }
        temp--;
        printf("\n");
    }
    temp++;
    temp++;
    for (i = n-2; i >=0; i--) {
        for (j = 0; j < i; j++) {
            printf("%d ", n - j);
        }
        for (j = 0; j < 2 * temp - 1; j++) {
            printf("%d ", temp);
        }
        for (j = i - 1; j >= 0; j--) {
            printf("%d ", n - j);
        }
        temp++;
        printf("\n");
    }
    // Complete the code to print the pattern.
    return 0;
}
