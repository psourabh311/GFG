import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        int i = 10;
        while(i > 0){
            System.out.print(number * i + " ");
            i--;
        }
        
        sc.close();
    }
}
