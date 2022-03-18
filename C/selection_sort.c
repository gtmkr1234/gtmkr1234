#include<stdio.h>
int main(){
    int n;
    printf("Enter the size of the array : \n");
    scanf("%d",&n);
    int arr[n];
    for(int i=0; i<n; i++){
        scanf("%d",&arr[i]);
    }
    for(int i=0; i<n; i++){
        int min = arr[i];
        int index=0;
        for(int j=i; j<n; j++){
            if(arr[j]<min){
                min = arr[j];
                index = j;
            }
        }
        if(min != arr[i]){
            int temp = arr[i];
            arr[i] = arr[index];
            arr[index] = temp;
        }
    }
    printf("Sorted Array : \n");
    for(int i=0; i<n; i++){
        printf("%d ",arr[i]);
    }
    }