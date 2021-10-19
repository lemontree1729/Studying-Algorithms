package p_1427;

import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String num = sc.next();
        int n = num.length();
        char[] digit = new char[n];
        for (int i = 0; i < n; i++) {
            digit[i] = num.charAt(i);
        }
        Arrays.sort(digit);
        String result = "";
        for (int j = 0; j < n; j++) {
            result += digit[n - 1 - j];
        }
        System.out.println(result);
        sc.close();
    }
}
