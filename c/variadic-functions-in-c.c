
int  sum (int count,...) {
    int i,sum=0;
    va_list pointer;
    va_start(pointer, count);
    for (i=0; i<count; i++) {
        sum+=va_arg(pointer, int);
    }
    va_end(pointer);
    return sum;
}

int min(int count,...) {
    int temp,i,min=0;
    va_list pointer;
    va_start(pointer, count);
    min=va_arg(pointer, int);
    for (i=0; i<count; i++) {
        temp=va_arg(pointer, int);
        if(min>temp)
            min=temp;
    }
    va_end(pointer);
    return min;
}

int max(int count,...) {
    int temp,i,max=0;
    va_list pointer;
    va_start(pointer, count);
    max=va_arg(pointer, int);
    for (i=0; i<count; i++) {
        temp=va_arg(pointer, int);
        if(max<temp)
            max=temp;
    }
    va_end(pointer);
    return max;
}

