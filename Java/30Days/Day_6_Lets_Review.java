import java.io.*;
import java.util.*;

public class Day_6_Lets_Review {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */

        Scanner scan = new Scanner(System.in);

        int T = Integer.parseInt(scan.nextLine());

        for (int i = 0; i < T; i++) {
            String S = scan.nextLine();
            char[] arr = S.toCharArray();
            for(int j = 0; j < arr.length; j += 2) {
                System.out.print(arr[j]);
            }
            System.out.print(" ");
            for(int j = 1; j < arr.length; j += 2) {
                System.out.print(arr[j]);
            }
            System.out.printf("\n");
            
        }
        scan.close();
    }
}