#include<stdio.h>

int main()
{
    int marks;
    printf("Enter the marks in Mathematics: ");
    scanf("%d", &marks);
    switch (marks)
    {
    case 40:
        printf("B");
        break;
    
    default:
        break;
    }
    return 0;
}