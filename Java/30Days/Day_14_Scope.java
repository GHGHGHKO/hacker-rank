import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


class Difference {
  	private int[] elements;
  	public int maximumDifference;

	// Add your code here
    Difference(int[] elements) {
        this.elements = elements;
    }

    public void computeDifference() {
        int result;
        maximumDifference = 0;
        for(int i = 0; i < elements.length; i++) {
            for(int element : elements) {
                result = Math.abs(element - elements[i]);
                if (result > maximumDifference) {
                    maximumDifference = result;
                }
            }
        }
        
    }

} // End of Difference class

public class Day_14_Scope {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        sc.close();

        Difference difference = new Difference(a);

        difference.computeDifference();

        System.out.print(difference.maximumDifference);
    }
}