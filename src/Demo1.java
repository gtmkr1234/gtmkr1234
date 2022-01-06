class Stu{
    static int rollno;
    static int arr[];
// We can alo private the constructor
    public static void Stu(int rollno1, int[] arr1) {
        rollno = rollno1;
        arr = arr1;
        //this.arr is an example of shallow copy
        // there is also a concept of deep copy
    }
    //Satatic - associated with the class not the objects
    static void display(){
        System.out.println(rollno);
        for(int res: arr){
            System.out.println(res);
        }

    }
}
public class Demo1 {
    public static void main(String[] args) {
       Stu.Stu(56,new int[]{23_000,56,45,78,98});
       Stu.display();
    }
}
// BigInteger class- to be studied(Predefined class in java){Dynamic memory allocation}
//BigDecimal class- to be studied(Predefined class in  java){Dynamic memory allocation}