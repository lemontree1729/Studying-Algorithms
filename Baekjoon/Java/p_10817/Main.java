package p_10817;

import java.util.Scanner;
import java.lang.Math;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] num = new int[3];
        num[0] = sc.nextInt();
        int maxnum = num[0];
        for (int i = 1; i < 3; i++) {
            num[i] = sc.nextInt();
            maxnum = Math.max(maxnum, num[i]);
        }
        for (int j = 0; j < 3; j++) {
            if (num[j] == maxnum) {
                System.out.println(Math.max(num[(j + 1) % 3], num[(j + 2) % 3]));
                break;
            }
        }
        sc.close();
    }
}
