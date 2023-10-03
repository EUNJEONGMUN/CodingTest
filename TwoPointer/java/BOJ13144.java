package TwoPointer.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class BOJ13144 {
    static int N;
    static int[] arr;
    static long answer; // 경우의 수가 int 범위 넘어감에 주의

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Set<Integer> exists = new HashSet<>();

        int left = 0;
        int right = 0;

        while (right < N) {
            if (exists.contains(arr[right])) {
                while (arr[left] != arr[right]) {
                    exists.remove(arr[left++]);
                }
                left++;
            }

            answer += right - left + 1;
            exists.add(arr[right++]);

        }
        System.out.println(answer);
    }
}
