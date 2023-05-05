package DynamicProgramming1.java;

import java.util.Scanner;

public class BOJ11726 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());

        long[] dp = new long[n + 1];
        if (n == 1) {
            System.out.println(1);
        } else if (n == 2) {
            System.out.println(2);
        } else {
            dp[1] = 1;
            dp[2] = 2;
            for (int i = 3; i < n + 1; i++) {
                dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
            }
            System.out.println(dp[n]);
        }
    }

}
