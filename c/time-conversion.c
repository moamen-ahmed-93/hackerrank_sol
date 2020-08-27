
#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();

/*
 * Complete the timeConversion function below.
 */

/*
 * Please either make the string static or allocate on the heap. For example,
 * static char str[] = "hello world";
 * return str;
 *
 * OR
 *
 * char* str = "hello world";
 * return str;
 *
 */
void convS(int x,char* c){
    int temp=x;
    x=x/10;

    c[0]=x+'0';
    x=temp-x*10;
    c[1]=x+'0';
}
char* timeConversion(char* s)
{
    /*
     * Write your code here.
     */
    char* op=malloc (1 + strlen (s));
    char temp[2];
    int x;
    strcpy(op,s);
    if(s[8]=='P')
    {
        temp[0]=op[0];
        temp[1]=op[1];
        x=atoi(temp);
        if(x!=12)
            x=x+12;
        convS(x,temp);
        op[0]=temp[0];
        op[1]=temp[1];

    }
    else  if(s[8]=='A')
    {
        if(s[0]=='1'&&s[1]=='2'){
            op[0]='0';
            op[1]='0';
        }

    }
    op[8]='\0';
    return op;
}


int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    char* s = readline();

    char* result = timeConversion(s);

    fprintf(fptr, "%s\n", result);

    fclose(fptr);

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) { break; }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }

        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);

        if (!data) { break; }

        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
    }

    data = realloc(data, data_length);

    return data;
}
