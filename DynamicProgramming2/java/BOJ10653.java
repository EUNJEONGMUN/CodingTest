package DynamicProgramming2.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ10653 {
    static int N, K;
    static int MAX_VALUE = 1234567890;
    static List<int[]> arr = new ArrayList<>();
    static int[][] dp;
    static int[][] dist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        dp = new int[N][K + 1];
        dist = new int[N][N];

        for (int[] ints : dp) {
            Arrays.fill(ints, -1);
        }


        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr.add(new int[]{a, b});
        }

        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                dist[i][j] = getDistance(i, j);
                dist[j][i] = dist[i][j];
            }

        }

        System.out.println(solution(N - 1, K));
    }

    private static int solution(int now, int k) {
        if (dp[now][k] != -1) return dp[now][k];
        if (now == 0) return 0;

        dp[now][k] = MAX_VALUE;

        for (int jump = 0; jump <= k; jump++) {
            if (now - jump - 1 < 0) {
                break;
            }
            dp[now][k] = Math.min(solution(now - jump - 1, k - jump) + dist[now - jump - 1][now], dp[now][k]);
        }
        return dp[now][k];

    }

    private static int getDistance(int x, int y) {
        return Math.abs(arr.get(x)[0] - arr.get(y)[0]) + Math.abs(arr.get(x)[1] - arr.get(y)[1]);
    }
}
