#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char* ltrim(char*);
char* rtrim(char*);
char** split_string(char*);

int parse_int(char*);

/*
 * Complete the 'getTotalX' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY a
 *  2. INTEGER_ARRAY b
 */

int getTotalX(int a_count, int* a, int b_count, int* b) {
 int j,i = 1, num_of_nums = 0, gcd = 1, flag = 0;
    gcd = a[a_count - 1];
    int* temp = (int*) malloc(sizeof(int) * a_count);
    for (i = 0; i < a_count; i++)
        temp[i] = a[i];
    int min = a[0], min_i = 0;
    for (i = 0; i < a_count; i++) {
        if (a[i] > b[0])
            return 0;
    }
    while (1) {
        for (i = 0; i < a_count; ++i) {

            if (temp[min_i] == temp[i])
                flag = 1;
            else {
                flag = 0;
                break;
            }

        }
        if (flag == 1)
            break;
        min = temp[0];
        min_i = 0;
        for (i = 0; i < a_count; ++i) {

            if (temp[i] < min) {
                min = temp[i];
                min_i = i;
            }

        }
        temp[min_i] += a[min_i];

    }
    gcd = temp[min_i];
    min = b[0];
    flag=0;

    for (i = 0; i < b_count; i++) {
        if (min > b[i])
            min = b[i];
    }
    i=1;
    while (i * gcd <= min) {
        for (j = 0; j < b_count; j++) {
            if((b[j]%(gcd * (i)))!=0){
                flag=0;
                break;
            }
            flag=1;
        }
        if(flag == 1)
            num_of_nums++;
        flag = 0;
        i++;
    }
    return num_of_nums;
}
int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    char** first_multiple_input = split_string(rtrim(readline()));
    
    int n = parse_int(*(first_multiple_input + 0));

    int m = parse_int(*(first_multiple_input + 1));

    char** arr_temp = split_string(rtrim(readline()));

    int* arr = malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        int arr_item = parse_int(*(arr_temp + i));

        *(arr + i) = arr_item;
    }

    char** brr_temp = split_string(rtrim(readline()));

    int* brr = malloc(m * sizeof(int));

    for (int i = 0; i < m; i++) {
        int brr_item = parse_int(*(brr_temp + i));

        *(brr + i) = brr_item;
    }

    int total = getTotalX(n, arr, m, brr);

    fprintf(fptr, "%d\n", total);

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

        if (!line) {
            break;
        }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') {
            break;
        }

        alloc_length <<= 1;

        data = realloc(data, alloc_length);

        if (!data) {
            data = '\0';

            break;
        }
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';

        data = realloc(data, data_length);

        if (!data) {
            data = '\0';
        }
    } else {
        data = realloc(data, data_length + 1);

        if (!data) {
            data = '\0';
        } else {
            data[data_length] = '\0';
        }
    }

    return data;
}

char* ltrim(char* str) {
    if (!str) {
        return '\0';
    }

    if (!*str) {
        return str;
    }

    while (*str != '\0' && isspace(*str)) {
        str++;
    }

    return str;
}

char* rtrim(char* str) {
    if (!str) {
        return '\0';
    }

    if (!*str) {
        return str;
    }

    char* end = str + strlen(str) - 1;

    while (end >= str && isspace(*end)) {
        end--;
    }

    *(end + 1) = '\0';

    return str;
}

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);

        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;

        token = strtok(NULL, " ");
    }

    return splits;
}

int parse_int(char* str) {
    char* endptr;
    int value = strtol(str, &endptr, 10);

    if (endptr == str || *endptr != '\0') {
        exit(EXIT_FAILURE);
    }

    return value;
}
