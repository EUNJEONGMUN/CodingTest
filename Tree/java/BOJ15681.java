package Tree.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ15681 {
    static int N, R, Q;
    static List<Integer>[] map;
    static int[] subCount;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        map = new ArrayList[N + 1];
        subCount = new int[N + 1];
        for (int i = 1; i < N + 1; i++) {
            map[i] = new ArrayList<>();
        }
        Arrays.fill(subCount, 1);

        for (long i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            map[a].add(b);
            map[b].add(a);
        }

        solution(R, -1);

        for (int i = 0; i < Q; i++) {
            System.out.println(subCount[Integer.parseInt(br.readLine())]);
        }
    }

    private static void solution(int idx, int parent) {
        for (Integer next : map[idx]) {
            if (parent != next) { // 왔던 곳 돌아가는 거 방지
                solution(next, idx);
            }
        }

        if (parent != -1) {
            subCount[parent] += subCount[idx];
        }
    }
}
