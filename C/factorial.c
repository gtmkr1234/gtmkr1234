#include<stdio.h>
long long int fact(int n){
    if(n<=1){
        return 1;
    }
    else{
        return n*fact(n-1);
    }
}
int main(){
    int n;
    printf("Enter the number : \n");
    scanf("%d",&n);
    long long int res = fact(n);
    printf("factorial is : %lld",res);
    return 0;
}