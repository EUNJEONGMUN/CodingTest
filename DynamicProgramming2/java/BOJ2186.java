package DynamicProgramming2.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ2186 {
    static int N, M, K;
    static String[] goal;
    static String[][] arr;
    static int[][][] dp;
    static int answer;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        arr = new String[N][M];

        for (int i = 0; i < N; i++) {
            String[] split = br.readLine().split("");
            for (int j = 0; j < M; j++) {
                arr[i][j] = split[j];
            }
        }

        goal = br.readLine().split("");

        dp = new int[N][M][goal.length];

        for (int[][] a : dp) {
            for (int[] b : a) {
                Arrays.fill(b, -1);
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (arr[i][j].equals(goal[0])) {
                    answer += solution(i, j, 0);
                }
            }
        }

        System.out.println(answer);
    }

    private static int solution(int x, int y, int L) {
        if (dp[x][y][L] != -1) {
            return dp[x][y][L];
        }
        if (L == goal.length - 1) {
            return dp[x][y][L] = 1;
        }

        dp[x][y][L] = 0;

        for (int dist = 1; dist <= K; dist++) {
            for (int dir = 0; dir < 4; dir++) {
                int nx = x + dx[dir] * dist;
                int ny = y + dy[dir] * dist;
                if (checkRange(nx, ny) && arr[nx][ny].equals(goal[L + 1])) {
                    dp[x][y][L] += solution(nx, ny, L + 1);
                }
            }
        }
        return dp[x][y][L];
    }

    private static boolean checkRange(int x, int y) {
        return x >= 0 && y >= 0 && x < N && y < M;
    }
}
