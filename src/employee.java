import java.util.*;
public class employee {
    String Name;
    int Yoj;
    String Address;
    Scanner sc=new Scanner(System.in);
    public void getName(){
        System.out.println("Enter the name of the Employee:");
        Name = sc.nextLine();
        System.out.println("Enter the year of joining: ");
        Yoj = sc.nextInt();
        System.out.println("Enter the addess of "+ Name);
        Address= sc.nextLine();
    }
    public void display(){

    }
}
