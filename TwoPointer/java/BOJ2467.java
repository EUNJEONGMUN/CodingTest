package TwoPointer.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ2467 {
    static int N;
    static int[] arr;
    static int diff = Integer.MAX_VALUE;
    static int A, B;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int left = 0;
        int right = N - 1;

        while (left < right) {
            if (Math.abs(arr[left] + arr[right]) < diff) {
                diff = Math.abs(arr[left] + arr[right]);
                A = arr[left];
                B = arr[right];
            }

            if (arr[left] + arr[right] > 0) {
                right--;
            } else {
                left++;
            }
        }

        System.out.println(A + " " + B);
    }
}
