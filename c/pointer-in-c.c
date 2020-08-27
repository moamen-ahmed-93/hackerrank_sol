#include <stdio.h>

void update(int *a,int *b) {
    // Complete this function
    int temp1,temp2;
    temp1= *a+*b;
    temp2= *a-*b;
    if(temp2<0)
        temp2=temp2*-1;
    *a=temp1;
    *b=temp2;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
