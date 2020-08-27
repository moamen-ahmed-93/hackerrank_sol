#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>



int main() 
{
    int i,a, b;
    char arr[9][10]={"one","two","three","four","five","six","seven","eight","nine"};
    scanf("%d\n%d", &a, &b);
  	// Complete the code.
    for (i=a; i<=9 && i<= b; i++) {
        printf("%s\n",arr[i-1]);
    }
    for (i=10; i<=b; i++) {
        if(i%2==0)
            printf("even\n");
        else
            printf("odd\n");
    }
    return 0;
}

