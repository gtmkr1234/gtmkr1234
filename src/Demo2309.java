class Emp{
    private int id;
    private int sal;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getSal() {
        return sal;
    }

    public void setSal(int sal) {
        this.sal = sal;
    }
}
public class Demo2309 {
    public static void main(String[] args) {
        Emp obj = new Emp();
        obj.setId(12);
        obj.setSal(12000);
        System.out.println(obj.getId());
        System.out.println(obj.getSal());
    }
}
