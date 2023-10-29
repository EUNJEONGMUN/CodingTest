package BruteForce.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ16637 {
    static int[] arr;
    static String[] op;
    static int answer = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        arr = new int[N / 2 + 1];
        op = new String[N / 2];
        String[] split = br.readLine().split("");
        int idx = 0;
        for (int i = 0; i < split.length; i++) {
            if (i % 2 == 0) {
                arr[idx] = Integer.parseInt(split[i]);
            } else {
                op[idx++] = split[i];
            }
        }
        solution(arr[0], 0);
        System.out.println(answer);
    }

    private static int calculate(String op, int a, int b) {
        switch (op) {
            case "+":
                return a + b;
            case "-":
                return a - b;
            case "*":
                return a * b;
        }
        return 0;
    }

    private static void solution(int result, int idx) {
        if (idx >= op.length) {
            answer = Math.max(answer, result);
            return;

        }

        int result1 = calculate(op[idx], result, arr[idx + 1]);
        solution(result1, idx + 1);

        if (idx + 1 < op.length) {
            int result2 = calculate(op[idx + 1], arr[idx + 1], arr[idx + 2]);

            solution(calculate(op[idx], result, result2), idx + 2);
        }
    }
}
