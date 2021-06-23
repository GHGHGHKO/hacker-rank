import java.io.*;
import java.util.*;

public class Day_25_Running_Time_and_Complexity {

    public static void isPrime(int element) {
        if(element < 2) {
            System.out.println("Not prime");
            return;
        }

        if(element == 2) {
            System.out.println("Prime");
            return;
        }

        for(int j = 2; j <= Math.sqrt(element); j++) {
            if(element % j == 0) {
                System.out.println("Not prime");
                return;                
            }
        }
        System.out.println("Prime");
        return;
    }

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */

        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        for(int i = 0; i < n; i++) {
            int element = scan.nextInt();
            isPrime(element);
        }
    }
}