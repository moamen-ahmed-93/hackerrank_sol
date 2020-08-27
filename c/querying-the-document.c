

char* kth_word_in_mth_sentence_of_nth_paragraph(char**** document, int k, int m, int n) {
    return document[n-1][m-1][k-1];
}

char** kth_sentence_in_mth_paragraph(char**** document, int k, int m) { 
    return document[m-1][k-1];
}

char*** kth_paragraph(char**** document, int k) {
    return document[k-1];
}

char**** get_document(char* text) {
    char ****doc=(char****)malloc(sizeof(char***)*5);
    int i,j,k,l;
    int wordIndx=0,charIndx=0,sentIndx=0,parIndx=0;
    for(i=0;i<5;i++){
        doc[i]=(char***)malloc(sizeof(char**)*5);
        for(j=0;j<100;j++){
            doc[i][j]=(char**)malloc(sizeof(char*)*100);
            for(k=0;k<1000;k++){
                doc[i][j][k]=(char*)malloc(sizeof(char)*1000);
            }
        }
    }
    l=0;
    for(i=0;i<1000;i++){
        if(text[i]=='\0')
            break;
        else if(text[i]=='\n'){
            doc[parIndx][sentIndx][wordIndx][charIndx]='\0';
            parIndx++;
            charIndx=0;
            sentIndx=0;
            wordIndx=0;
        }
        else if(text[i]=='.'){
            doc[parIndx][sentIndx][wordIndx][charIndx]='\0';
            charIndx=0;
            wordIndx=0;
            sentIndx++;
        }
        else if(text[i]==' '){
            doc[parIndx][sentIndx][wordIndx][charIndx]='\0';
            charIndx=0;
            wordIndx++;
            
        }
        else {
            doc[parIndx][sentIndx][wordIndx][charIndx++]=text[i];
            
        }
    }
    
    return doc;
}

