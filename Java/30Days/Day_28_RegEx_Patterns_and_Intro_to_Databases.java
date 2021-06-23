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

public class Day_28_RegEx_Patterns_and_Intro_to_Databases {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(bufferedReader.readLine().trim());
        ArrayList<String> saveName = new ArrayList<String>();

        IntStream.range(0, N).forEach(NItr -> {
            try {
                String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

                String firstName = firstMultipleInput[0];

                String emailID = firstMultipleInput[1];

                String[] isGmail = emailID.split("@");

                if(isGmail[1].equals("gmail.com")) {
                    saveName.add(firstName);
                }
                
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });
        Collections.sort(saveName);

        for(String i : saveName) {
            System.out.println(i);
        }

        bufferedReader.close();
    }
}
