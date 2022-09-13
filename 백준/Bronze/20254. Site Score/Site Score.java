import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int ur = sc.nextInt();
        int tr = sc.nextInt();
        int uo = sc.nextInt();
        int to = sc.nextInt();
        System.out.println(ur*56+tr*24+uo*14+to*6);
    }
}