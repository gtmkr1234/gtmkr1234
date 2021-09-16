#include<stdio.h>
#include<conio.h>
int main(){
    int a =15,b = 30, temp;
    temp=a;
    a=b;
    b=temp;
    printf("%d %d",a,b);
    return 0;
}