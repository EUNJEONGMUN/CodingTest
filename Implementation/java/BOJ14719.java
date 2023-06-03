package Implementation.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ14719 {
    static int H, W;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        H = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());
        arr = new int[W];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < W; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int left = 0, right = W-1;
        int max_left = arr[left], max_right = arr[right];
        int answer = 0;

        while (left < right) {
            max_left = Math.max(max_left, arr[left]);
            max_right = Math.max(max_right, arr[right]);

            if (max_left <= max_right) {
                answer += max_left-arr[left];
                left++;
            } else {
                answer += max_right-arr[right];
                right--;
            }
        }

        System.out.println(answer);

    }
}
