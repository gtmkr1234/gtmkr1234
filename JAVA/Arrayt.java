import java.util.*;
class stu{
    int Rollno;
    String name;
    int marks[];
    Scanner inp= new Scanner(System.in);
    stu(){
        Rollno=10;
        name="Krishna";
        marks= new int[5];
        for(var i=0; i<marks.length; i++){
            marks[i]= inp.nextInt();
        }
    }
    public void display(){
        System.out.println(Rollno);
        System.out.println(name);
        for(int res: marks){
            System.out.println(res + "\n");
        }
    }
}
class Main{
    public static void main(String[] args) {
        stu arr[]=new stu[2];
        for(var i=0; i<arr.length; i++){
            arr[i]= new stu();
        }
        for(var i=0; i<arr.length; i++){
            arr[i].display();
        }
    }
}