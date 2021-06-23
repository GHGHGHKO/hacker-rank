import java.io.*;
import java.util.*;

public class Day_26_Nested_Logic {

    static int getHackos(int returnedYear,
                        int returnedMonth,
                        int returnedDay,
                        int dueYear,
                        int dueMonth,
                        int dueDay) {
                            if (returnedYear > dueYear)     return 10000;
                            if (returnedYear < dueYear)     return 0;
                            if (returnedMonth > dueMonth)   return (returnedMonth - dueMonth) * 500;
                            if (returnedMonth < dueMonth)   return 0;
                            if (returnedDay > dueDay)       return (returnedDay - dueDay) * 15;
                            if (returnedDay < dueDay)       return 0;

                            return 0;
                        }

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */

        Scanner scan = new Scanner(System.in);

        int returnedDay = scan.nextInt();
        int returnedMonth = scan.nextInt();
        int returnedYear = scan.nextInt();
        int dueDay = scan.nextInt();
        int dueMonth = scan.nextInt();
        int dueYear = scan.nextInt();

        System.out.println(getHackos(returnedYear,
        returnedMonth,
        returnedDay,
        dueYear,
        dueMonth,
        dueDay));
    }
}