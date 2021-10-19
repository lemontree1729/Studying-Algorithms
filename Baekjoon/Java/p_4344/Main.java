package p_4344;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int c = sc.nextInt();
        for (int i = 0; i < c; i++) {
            int n = sc.nextInt();
            double sum = 0;
            int[] score = new int[n];
            for (int j = 0; j < n; j++) {
                score[j] = sc.nextInt();
                sum += score[j];
            }
            double mean = sum / score.length;
            double cnt = 0;
            for (int k : score) {
                if (k > mean) {
                    cnt++;
                }
            }
            System.out.println(String.format("%.3f", cnt / score.length * 100.0) + "%");
            sc.close();
        }
    }
}
