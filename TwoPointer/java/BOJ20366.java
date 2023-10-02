package TwoPointer.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ20366 {
    static int N;
    static int[] arr;
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        for (int left = 0; left<N-1; left++) {
            for (int right = left+1; right<N; right++) {

                answer = Math.min(answer, getDiff(left, right));
            }
        }

        System.out.println(answer);
    }

    private static int getDiff(int left, int right) {
        int res = Integer.MAX_VALUE;
        int start = 0;
        int end = N-1;

        int value = arr[left]+arr[right];

        while (start<end) {
            if (start == left|| start == right) {
                start++;
            } else if (end == left || end == right) {
                end--;
            } else {
                res = Math.min(res, Math.abs(value-(arr[start]+arr[end])));
                if (value > arr[start]+arr[end]) {
                    start++;
                } else if (value < arr[start]+arr[end]){
                    end--;
                } else {
                    break;
                }
            }
        }
        return res;
    }
}
