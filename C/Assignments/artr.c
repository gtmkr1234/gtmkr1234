#include<stdio.h>
#include<math.h>
void main(){
    float a, b, h, area;
    printf("Enter the praallel sides of Trapezium \n");
    scanf("%f%f", &a, &b);
    printf("Enter the height of Trapezium \n");
    scanf("%f", &h);
    area = (a+b)*(h/2);
    printf(" Area of the trapezium is = %f", area);
}
