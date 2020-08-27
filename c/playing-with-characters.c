#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char c;
    char s[100];
    char s2[100];
    scanf("%c",&c);
    scanf("%s",s);
    scanf("\n");
    scanf("%[^\n]%*c", s2);
    printf("%c\n%s\n%s",c,s,s2);    
    return 0;
}
