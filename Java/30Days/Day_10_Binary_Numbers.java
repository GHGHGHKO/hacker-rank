import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



public class Day_10_Binary_Numbers {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        String n2 = Integer.toBinaryString(n);
        char[] n2Arr = n2.toCharArray();
        int result = 1, cnt = 1;
        for (int i = 1; i < n2Arr.length; i++) {
            if (n2Arr[i - 1] == n2Arr[i]) {
                cnt += 1;
                if (result < cnt) {
                    result = cnt;
                }
            } else {
                cnt = 1;
                
            }
        }

        System.out.println(result);
        


        bufferedReader.close();
    }
}
