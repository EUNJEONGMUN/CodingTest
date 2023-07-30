package GraphTraversal.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ9177 {
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String first = st.nextToken();
            String second = st.nextToken();
            String third = st.nextToken();

            if (solution(first, second, third)) {
                System.out.println(String.format("Data set %d: yes", i + 1));
            } else {
                System.out.println(String.format("Data set %d: no", i + 1));
            }
        }
    }

    private static boolean solution(String first, String second, String third) {
        int[][] dp = new int[4][third.length() + 1];
        for (int i = 0; i < 4; i++) {
            dp[i][0] = 0;
        }
        for (int i = 1; i < third.length() + 1; i++) {
            boolean flag1 = false;
            boolean flag2 = false;
            
            // first를 먼저 움직였을 때
            if (dp[0][i - 1] < first.length() && third.charAt(i - 1) == first.charAt(dp[0][i - 1])) {
                dp[0][i] = dp[0][i - 1] + 1;
                dp[1][i] = dp[1][i - 1];
                flag1 = true;
            } else if (dp[1][i - 1] < second.length() && third.charAt(i - 1) == second.charAt(dp[1][i - 1])) {
                dp[0][i] = dp[0][i - 1];
                dp[1][i] = dp[1][i - 1] + 1;
                flag2 = true;

            }

            // second를 먼저 움직였을 때
            if (dp[3][i - 1] < second.length() && third.charAt(i - 1) == second.charAt(dp[3][i - 1])) {
                dp[3][i] = dp[3][i - 1] + 1;
                dp[2][i] = dp[2][i - 1];
                flag2 = true;
            } else if (dp[2][i - 1] < first.length() && third.charAt(i - 1) == first.charAt(dp[2][i - 1])) {
                dp[3][i] = dp[3][i - 1];
                dp[2][i] = dp[2][i - 1] + 1;
                flag2 = true;
            }

            if (!flag1 && !flag2) {
                return false;
            }

            if (flag1 && !flag2) {
                dp[2][i] = dp[0][i];
                dp[3][i] = dp[1][i];
            } else if (!flag1 && flag2) {
                dp[0][i] = dp[2][i];
                dp[1][i] = dp[3][i];
            }
            System.out.println("=========");
            for (int k = 0; k < 4; k++) {
                System.out.println(Arrays.toString(dp[k]));
            }
        }
        return true;
    }
}
