package DynamicProgramming2.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ17404 {
    static int N;
    static int R = 0;
    static int G = 1;
    static int B = 2;
    static int[][] cost;
    static int[][] dp;
    static int answer = Integer.MAX_VALUE;
    static int MAX_VALUE = 1000 * 1000 + 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        cost = new int[N][3];
        dp = new int[N][3];

        StringTokenizer st;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            cost[i][0] = Integer.parseInt(st.nextToken());
            cost[i][1] = Integer.parseInt(st.nextToken());
            cost[i][2] = Integer.parseInt(st.nextToken());
        }

        for (int start : List.of(R, G, B)) {
            // 첫 번째 집 색 고정
            for (int init : List.of(R, G, B)) {
                if (init == start) {
                    dp[0][init] = cost[0][init];
                } else {
                    dp[0][init] = MAX_VALUE;
                }
            }

            for (int i = 1; i < N; i++) {
                dp[i][R] = Math.min(dp[i - 1][G], dp[i - 1][B]) + cost[i][R];
                dp[i][G] = Math.min(dp[i - 1][R], dp[i - 1][B]) + cost[i][G];
                dp[i][B] = Math.min(dp[i - 1][R], dp[i - 1][G]) + cost[i][B];
            }

            for (int end : List.of(R, G, B)) {
                if (end == start) {
                    continue;
                }
                answer = Math.min(answer, dp[N - 1][end]);
            }
        }

        System.out.println(answer);
    }

}
