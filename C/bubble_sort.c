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
        for(int j=0; j<n; j++){
            if(arr[i]<arr[j]){
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    printf("Sorted Array : \n");
    for(int i=0; i<n; i++){
        printf("%d ",arr[i]);
    }
}