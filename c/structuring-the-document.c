
typedef struct document document;
typedef struct paragraph paragraph;
typedef struct sentence sentence;
typedef struct word word;

struct document get_document(char* text) {
    document doc;
    doc.data=(paragraph*)malloc(sizeof(paragraph)*5);
    int i,j,k,l;
    int wordIndx=0,charIndx=0,sentIndx=0,parIndx=0;
    for(i=0;i<5;i++){
        //doc.data[i]=(paragraph*)malloc(sizeof(paragraph)*5);
        doc.data[i].data=(sentence*)malloc(sizeof(sentence)*5);
        for(j=0;j<100;j++){
            doc.data[i].data[j].data=(word*)malloc(sizeof(word)*100);
            for(k=0;k<1000;k++){
                doc.data[i].data[j].data[k].data=(char*)malloc(sizeof(char)*1000);
            }
        }
    }
    l=0;
    for(i=0;i<1000;i++){
        if(text[i]=='\0')
            break;
        else if(text[i]=='\n'){
            doc.data[parIndx].data[sentIndx].data[wordIndx].data[charIndx]='\0';
            doc.data[parIndx].data[sentIndx].word_count=++wordIndx;
            //doc.data[parIndx].sentence_count= ++sentIndx;
            doc.paragraph_count= ++parIndx;
            charIndx=0;
            sentIndx=0;
            wordIndx=0;
        }
        else if(text[i]=='.'){
            doc.data[parIndx].data[sentIndx].data[wordIndx].data[charIndx]='\0';
            doc.data[parIndx].data[sentIndx].word_count=++wordIndx;
            charIndx=0;
            wordIndx=0;
            doc.data[parIndx].sentence_count= ++sentIndx;
        }
        else if(text[i]==' '){
            doc.data[parIndx].data[sentIndx].data[wordIndx].data[charIndx]='\0';
            charIndx=0;
            doc.data[parIndx].data[sentIndx].word_count=++wordIndx;
        }
        else {
            doc.data[parIndx].data[sentIndx].data[wordIndx].data[charIndx++]=text[i];
        }
    }
    return doc;
}

struct word kth_word_in_mth_sentence_of_nth_paragraph(struct document Doc, int k, int m, int n) {
    return Doc.data[n-1].data[m-1].data[k-1];
}

struct sentence kth_sentence_in_mth_paragraph(struct document Doc, int k, int m) { 
    return Doc.data[m-1].data[k-1];
}

struct paragraph kth_paragraph(struct document Doc, int k) {
    return Doc.data[k-1];
}

