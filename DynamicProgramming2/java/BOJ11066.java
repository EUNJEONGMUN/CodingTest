package DynamicProgramming2.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ11066 {
    static int T;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            int[] arr = new int[N + 1];
            int[] sum = new int[N + 1];
            sum[0] = 0;
            for (int i = 1; i < N + 1; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
                sum[i] = sum[i - 1] + arr[i];
            }
            solution(arr, sum);
        }
    }

    private static void solution(int[] arr, int[] sum) {
        int[][] dp = new int[arr.length][arr.length];

        for (int k = 1; k < arr.length; k++) {
            for (int start = 1; start + k < arr.length; start++) {
                int end = start + k;
                dp[start][end] = Integer.MAX_VALUE;
                for (int idx = start; idx < end; idx++) {
                    dp[start][end] = Math.min(dp[start][end], dp[start][idx] + dp[idx + 1][end] + sum[end] - sum[start - 1]);

                }
            }
        }
        System.out.println(dp[1][arr.length - 1]);
    }
}
