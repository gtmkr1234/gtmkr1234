#include<stdio.h>
#include<conio.h>
#include<math.h>

int main(){
    int k1, k2, k3, k4, e1, e2, e3, e4, r1, r2, r3, r4, remch;
    scanf("%d %d %d %d", &k1, &k2, &k3, &k4);
scanf("%d %d %d %d", &e1, &e2, &e3, &e4); 
r1=k1-e1;
r2=k2-e2;
r3=k3-e3;
r4=k4-e4;
remch=r1+r2+r3+r4;
printf("The remaining chocolates are: %d", remch);
return 0;
getch();

}