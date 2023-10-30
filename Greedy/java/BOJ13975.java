package Greedy.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ13975 {
    static int T;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            Queue<Long> queue = new PriorityQueue<>();
            for (int i = 0; i < N; i++) {
                queue.offer(Long.parseLong(st.nextToken()));
            }
            long sum = 0;
            while (queue.size() > 1) {
                long a = queue.poll();
                long b = queue.poll();
                sum += a + b;
                queue.offer(a + b);
            }
            System.out.println(sum);
        }
    }
}
