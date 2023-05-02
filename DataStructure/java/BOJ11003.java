package DataStructure.java;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class BOJ11003 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        Deque<Node> deque = new ArrayDeque<>();
        for (int i = 0; i < N; i++) {
            Node now = new Node(i, Integer.parseInt(st.nextToken()));
            while (!deque.isEmpty() && deque.peekLast().value >= now.value) {
                deque.removeLast();
            }
            deque.addLast(now);
            if (deque.peekFirst().idx <= i - L) {
                deque.removeFirst();
            }
            bw.write(deque.peekFirst().value + " ");
        }
        bw.flush();
        bw.close();
    }

    static class Node {

        int idx;
        int value;

        Node(int idx, int value) {
            this.idx = idx;
            this.value = value;
        }
    }
}
