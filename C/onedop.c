#include<stdio.h>

int main()
{
    int n;
    int arr[n+5];
    printf("Enter the size of your array : \n");
    scanf("%d",&n);
    for(int i=0; i< n; i++){
        scanf("%d", &arr[i]);
    }   
    int pos,value;
    printf("Enter the value you want to insert : \n");
    scanf("%d",&value);
    printf("Enter the position at which you want to insert the value\n");
    scanf("%d",&pos);
    if(pos>n){
        printf("Invalid output!!!");
    }
    else{
        for(int i = n-1; i>=pos-1 ; i--){
            arr[i+1] = arr[i];
        }
        arr[pos - 1] = value;

        for(int i=0; i< n+1 ; i++){
            printf("%d ",arr[i]);
        }
    }
    return 0;
}
