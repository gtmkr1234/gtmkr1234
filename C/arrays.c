#include<stdio.h>
int main()
{
    int n;
    printf("Enter the size of the array : \n");
    scanf("%d",&n);
    int arr[n];
    for(int i=0; i<n; i++){
        arr[i] = 0;
        //Setting the default value to 0
    }
    for(int i=0; i<n; i++){
        printf("%d \n",arr[i]);
    }
    return 0;
}
