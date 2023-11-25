package Greedy.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ9576 {
    static int TC, N, M;
    static boolean[] check;
    static List<int[]> arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        TC = Integer.parseInt(br.readLine());
        StringTokenizer st;

        for (int tc = 0; tc < TC; tc++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            check = new boolean[N + 1];
            arr = new ArrayList<>();

            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                arr.add(new int[]{Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())});
            }

            Collections.sort(arr, (a, b) -> {
                return a[1] - b[1];
            }); // b 기준으로 오름차순 정렬

            int answer = 0;

            for (int[] ints : arr) {
                for (int i = ints[0]; i <= ints[1]; i++) {
                    if (!check[i]) {
                        check[i] = true;
                        answer++;
                        break;
                    }
                }
            }
            System.out.println(answer);
        }

    }
}