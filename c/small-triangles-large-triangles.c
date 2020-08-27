
void swap(float *xp, float *yp) 
{ 
    float temp = *xp; 
    *xp = *yp; 
    *yp = temp; 
}
void swapTr(triangle *xp, triangle *yp) 
{ 
    triangle temp = *xp; 
    *xp = *yp; 
    *yp = temp; 
} 
  
// A function to implement bubble sort 
void bubbleSort(float* arr,triangle* tr, int n) 
{ 
   int i, j; 
   for (i = 0; i < n-1; i++)       
  
       // Last i elements are already in place    
       for (j = 0; j < n-i-1; j++)  
           if (arr[j] > arr[j+1]){ 
              swap(&arr[j], &arr[j+1]);
              swapTr(&tr[j], &tr[j+1]); 
           }
} 
void sort_by_area(triangle* tr, int n) {
	float *areas=(float*)malloc(sizeof(float)*n);
    int i;
    float p;
    
    for (i=0; i<n; i++) {
        p=(tr[i].a*1.0+tr[i].c*1.0+tr[i].b*1.0)/2.0;
        areas[i]=sqrt(p*(p-tr[i].a*1.0)*(p-tr[i].b*1.0)*(p-tr[i].c*1.0));
    }
    /**
	* Sort an array a of the length n
	*/
    bubbleSort(areas,tr, n);
}

