#include<stdio.h>
int main()
{
    int n;
    printf("Enter the number of students :\n");
    scanf("%d", &n);
    int roll[n];
    if (n<=10){
        for(int i=0;i<n;i++){
            printf("\nEnter the roll number of student number - %d \n",i+1);
            scanf("%d",&roll[i]);
        }
        int quiz1[n];
        for(int i=0;i<n;i++){
           printf("\nEnter the marks of quiz 1 of student number - %d \n",i+1);
            scanf("%d",&quiz1[i]); 
        }
        int quiz2[n];
        for(int i=0;i<n;i++){
           printf("\nEnter the marks of quiz 2 of student number - %d \n",i+1);
            scanf("%d",&quiz2[i]); 
        }
        int quiz3[n];
        for(int i=0;i<n;i++){
           printf("\nEnter the marks of quiz 3 of student number - %d \n",i+1);
            scanf("%d",&quiz3[i]); 
        }
        int query;
        int index=0;
        printf("\nenter the roll number of student :");
        scanf("%d",&query);
        for(index=0; index<=n; index++){
        if (query==roll[index])
        break;
        }
        printf("\nMarks in quiz1 - %d, quiz2 - %d and quiz3 - %d",quiz1[index],quiz2[index],quiz3[index]);
        
        
    }
    else{
        printf("\nThe number of students can't be more than 10");
    }
    return 0;
}