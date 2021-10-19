package p_11021;

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int temp;
        for (int i = 1; i < n + 1; i++) {
            temp = sc.nextInt() + sc.nextInt();
            System.out.println("Case #" + i + ": " + temp);
        }
        sc.close();
    }
}
