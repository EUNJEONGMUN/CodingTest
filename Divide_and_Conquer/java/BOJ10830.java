package Divide_and_Conquer.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ10830 {
    static int N;
    static long B;
    static int[][] arr;
    static int MOD = 1000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        B = Long.parseLong(st.nextToken());
        arr = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken()) % MOD;
            }
        }

        int[][] answer = solution(arr, B);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(answer[i][j] + " ");
            }
            System.out.println();
        }
    }

    private static int[][] solution(int[][] arr, long n) {
        if (n == 1) {
            return arr;
        }

        int[][] res = solution(arr, n / 2);
        res = calculate(res, res);

        if (n % 2 == 1) {
            res = calculate(res, arr);
        }
        return res;
    }

    private static int[][] calculate(int[][] arr1, int[][] arr2) {
        int[][] res = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < N; k++) {
                    res[i][j] += arr1[i][k] * arr2[k][j];
                    res[i][j] %= MOD;
                }
            }
        }
        return res;
    }
}
