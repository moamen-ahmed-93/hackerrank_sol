

int main()
{
    int total_number_of_shelves;
    int *page_index;
    scanf("%d", &total_number_of_shelves);
    int i;
    int total_number_of_queries;
    scanf("%d", &total_number_of_queries);
    total_number_of_books=(int*)malloc(sizeof(int)*total_number_of_shelves);
    for (i=0; i<total_number_of_shelves; i++) {
        total_number_of_books[i]=0;
    }
    total_number_of_pages=(int**)malloc(sizeof(int*)*total_number_of_shelves);
    for(i=0;i<total_number_of_shelves;i++){
        total_number_of_pages[i]=(int*)malloc(sizeof(int)*1100);
    }
    while (total_number_of_queries--) {
        int type_of_query;
        scanf("%d", &type_of_query);
        if (type_of_query == 1) {
            int x, y;
            scanf("%d %d", &x, &y);
            total_number_of_pages[x][total_number_of_books[x]++]=y;

