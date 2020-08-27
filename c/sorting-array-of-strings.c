
void swap2(char * s1, char* s2,int len) {
    int i;
    char* temp = (char*) malloc(sizeof(char) * len);
    //char* temp2 = (char*) malloc(sizeof(char) * len);
    for (i = 0; i < len; i++) {
        temp[i] = s1[i];
    }
    temp[i] = '\0';
    for (i = 0; i < len; i++) {
        s1[i] = s2[i];
    }
    s1[i] = '\0';
    //temp2=(char*)realloc(s2,len);
    for (i = 0; i < len; i++) {
        s2[i] = temp[i];
    }
    s2[i] = '\0';
    
}
void swapStr(char * s1, char* s2) {
    //printf("%s %s before\n",s1,s2);
    /*char temp[2500];
     strcpy(temp, s1);
     strcpy(s1, s2);
     strcpy(s2, temp);*/
    //printf("%s %s after\n",s1,s2);
   
    if (strlen(s1) >= strlen(s2)) {
        swap2(s1,s2,strlen(s1));
    }
    else{
        swap2(s1,s2,strlen(s2));
    }
}
int lexicographic_sort(const char* a, const char* b) {
    int x=strcmp(a, b);
    //printf("%s %s %d\n",a,b,x);
    if(x>0)
        return 1;
    return 0;
}

int lexicographic_sort_reverse(const char* a, const char* b) {
    int x=strcmp(a, b);
    if(x<0)
        return 1;
    return 0;
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    int i,j;
    int unique=1;
    int countA=0,countB=0;
    for (i=0; i<strlen(a)-1; i++) {
        for(j=i+1;j<strlen(a);j++){
                if(a[i]==a[j]){
                    unique=0;
                    break;
            }
        }
        if(unique==1)
            countA++;
        unique=1;
    }
    for (i=0; i<strlen(b)-1; i++) {
        for(j=i+1;j<strlen(b);j++){
                if(b[i]==b[j]){
                    unique=0;
                    break;
            }
        }
        if(unique==1)
            countB++;
        unique=1;
    }
    //printf("%s=%d %s=%d\n",a,countA,b,countB);
    if(countA>countB){
        return 1;
    }
    if(countA==countB ){
        
        int x=strcmp(a, b);
        //printf("%s %s %d\n",a,b,x);
        if(x>0)
            return 1;
        return 0;
    }
    return 0;
}

int sort_by_length(const char* a, const char* b) {
    int i=0;
    while(a[i]!='\0'){
        if(b[i]=='\0')
            return 1;
        i++;
    }
    if(b[i]=='\0'){
        
        int x=strcmp(a, b);
        if(x>0)
            return 1;
        return 0;
    }
    return 0;
}

void string_sort(char** arr, const int len,int (*cmp_func)(const char* a, const char* b)) {
    int sorted = 0;
    int top = len - 1;
    while (!sorted) {
        sorted = 1;
        for (int i = 0; i < top; i++) {
            if (cmp_func(arr[i], arr[i + 1]) > 0) {
                char *tmp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = tmp;
                sorted = 0;
            }
        }
        top--;
    }
}

