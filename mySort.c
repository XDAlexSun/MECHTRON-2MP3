#include <stdio.h>
#include <stdlib.h>

void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

// Bubble Sort
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {   //iterating to include cumulatively
            if (arr[j] > arr[j + 1])     swap(&arr[j], &arr[j + 1]);    //swapping if it is not in order
        }
    }
}

//Insertion Sort
void insertionSort(int arr[], int n){
    for(int i = 1; i < n; i++){
        int temp = arr[i];
        int j = i-1;
        while(j>=0&&arr[j]>temp){   //keep moving the current element until it is either in its right place or reaches start
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=temp;
    }
}

//Merge Sort
void merge(int arr[], int l, int m, int r){
    int n1= m-l+1;  //splitting the array
    int n2 = r-m;
    int *L = (int *)malloc(n1 * sizeof(int));
    int *R = (int *)malloc(n2 * sizeof(int));
    //writing the elements into the array
    for(int i =0; i<n1;i++){
        L[i]=arr[l+i];
    }
    for(int i =0; i<n2;i++){
        R[i]=arr[m+1+i];    
    }
    int i =0, j=0,k=l;
    //remapping the sorted elements of the new arrays back into the old one
    while(i<n1&&j<n2){
        if(L[i]<=R[j]){
            arr[k]=L[i];
            i++;
        }
        else{
            arr[k]=R[j];
            j++;
        }
        k++;
    }
    free(L);
    free(R);
}

void mergeSort(int arr[], int l, int r){
    if (l<r){
        int m = l+ (r-l)/2; //recursively calling merge and mergeSort until it is sorted
        mergeSort(arr, l, m);
        mergeSort(arr,m+1,r);
        merge(arr,l,m,r);
    }
}

//Heap Sort
void heapify(int arr[], int n, int i){
    int largest = i; 
    int l = 2* i +1, r = 2*i+2; //creating nodes
    if(l<n && arr[l]>arr[largest]) largest=l;   
    if(r<n && arr[r]>arr[largest]) largest=r;
    if (largest!=i){    
        int temp = arr[i];
        arr[i]=arr[largest];    //sorting the heap
        arr[largest]=temp;
        heapify(arr, n, largest);   //recursion
    }
}

void heapSort(int arr[], int n){
    for(int i = n/2-1; i>=0;i--){
        heapify(arr,n,i);       //creating many heaps
    }
    for(int i = n-1; i>0; i--){
        int temp = arr[0];
        arr[0]=arr[i];
        arr[i]=temp;        //recombinign the heaps
        heapify(arr,i,0);
    }
}

void countingSort(int *arr, int n) {    //coded with help from sina forouzanfar -- had old code that worked the same way but did this for optimziation
    int min = arr[0], max = arr[0]; //normally min is not needed but it is required for negative numbers
    for(int i = 1; i < n; i++){ //find max and min
        if (arr[i]>max) max=*(arr+i);
        if (arr[i]<min) min=*(arr+i);
    }
    int range = max-min+1;  //create the size of the zero array
    int *zArr = (int *)calloc(range, sizeof(int));
    for (int i = 0; i < n; i++) {
        int pos = *(arr+i) - min;           //assigning element of an index to a respective index (i.e. 4 at 5 to 5 at 4)
        *(zArr + pos) = *(zArr + pos) +1;   
    }
    int k = 0;
    for(int i = 0; i < range; i++){
        while(zArr[i]!=0){
            *(arr+k)=min+i; //adding subsequent reoccuring entries
            zArr[i]--;
            k++;
        }
    }
    free(zArr);
}


