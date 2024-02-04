package DynamicProgramming1.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ2011 {
    static int MOD = 1000000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String N = br.readLine().trim();
        int[] dp = new int[N.length() + 1];
        Arrays.fill(dp, 0);

        if (N.charAt(0) == '0') {
            System.out.println(0);
        } else {
            dp[0] = 1;
            dp[1] = 1;
            for (int i = 2; i <= N.length(); i++) {
                boolean isZero = false;

                if (N.charAt(i - 1) == '0') {
                    isZero = true;
                }

                int beforeNum = Integer.parseInt(N.substring(i - 2, i));
                if (beforeNum < 10) {
                    if (isZero) {
                        break;
                    }
                    dp[i] = (dp[i - 1]) % MOD;
                } else if (beforeNum <= 26) {
                    if (isZero) {
                        dp[i] = (dp[i - 2]) % MOD;
                    } else {
                        dp[i] = (dp[i-1] + dp[i - 2]) % MOD;
                    }
                } else {
                    if (!isZero) {
                        dp[i] = (dp[i - 1]) % MOD;
                    }
                }
            }
            System.out.println(dp[N.length()]);
        }
    }
}
/**
 * 도움 된 반례
 */
// 121074110 -> 2
// 305 -> 0
// 111012 -> 4