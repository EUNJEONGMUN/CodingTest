package Greedy.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class BOJ1715 {
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> queue = new PriorityQueue<>();

        for (int i = 0; i < N; i++) {
            queue.add(Integer.parseInt(br.readLine()));
        }

        int answer = 0;
        while (queue.size() > 1) {
            int card1 = queue.poll();
            int card2 = queue.poll();
            answer += card1 + card2;
            queue.offer(card1 + card2);

        }
        System.out.println(answer);

    }
}
