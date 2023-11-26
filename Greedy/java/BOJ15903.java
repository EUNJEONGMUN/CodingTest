package Greedy.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ15903 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        PriorityQueue<Long> queue = new PriorityQueue<>();

        for (int i = 0; i < N; i++) {
            queue.offer(Long.parseLong(st.nextToken()));
        }

        while (M-- > 0) {
            long a = queue.poll();
            long b = queue.poll();
            queue.offer(a + b);
            queue.offer(a + b);
        }

        long answer = queue.stream().mapToLong(Long::new).sum();
        System.out.println(answer);

        // 10^6 * 10^3 * 15 => long
    }
}