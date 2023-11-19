package DynamicProgramming1.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ15988 {
    static int T;
    static int MOD = 1000000009;
    static long[] dp = new long[1000001];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        solution();
        for (int tc = 0; tc < T; tc++) {
            int N = Integer.parseInt(br.readLine());
            System.out.println(dp[N]);
        }
    }

    private static void solution() {
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;
        for (int i = 4; i < 1000001; i++) {
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD;
        }
    }
}
