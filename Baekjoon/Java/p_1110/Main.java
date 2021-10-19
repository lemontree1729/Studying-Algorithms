package p_1110;

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int cnt = 0;
        int newnum = num;
        while (num != newnum || cnt == 0) {
            cnt++;
            int units = newnum % 10;
            int tens = newnum / 10;
            newnum = units * 10 + (tens + units) % 10;
        }
        System.out.println(cnt);
        sc.close();
    }
}
