#include<stdio.h>
#include<conio.h>
#include<math.h>

int main(){
    int a, b, c, h, area, perimeter;
    scanf("%d %d", &a, &b, &c);
    h=(a+b+c)/3;
    area=(h(h-a)(h-b)(h-c))^(1/2);
    printf("%d", area);
    return 0; 
    getch();
}