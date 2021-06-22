//Complete this code or write your own from scratch
import java.util.*;
import java.io.*;

class Day_8_Dictionaries_and_Maps{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Hashtable<String, Integer> hashTable = new Hashtable<String, Integer>();
        for(int i = 0; i < n; i++){
            String name = in.next();
            int phone = in.nextInt();
            // Write code here
            // save hash
            hashTable.put(name, phone);
        }
        while(in.hasNext()){
            String s = in.next();
            // Write code here
            // output hash
            if (hashTable.get(s) == null) {
                System.out.println("Not found");
            } else {
                System.out.println(s + "=" + hashTable.get(s));
            }
        }
        in.close();
    }
}