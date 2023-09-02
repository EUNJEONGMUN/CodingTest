package GraphTraversal.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ14267 {
    static int N, M;
    static List<Node> nodes = new ArrayList<>();
    static int[] answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        answer = new int[N + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < N + 1; i++) {
            nodes.add(new Node(i, Integer.parseInt(st.nextToken())));
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int idx = Integer.parseInt(st.nextToken());
            int point = Integer.parseInt(st.nextToken());
            nodes.get(idx - 1).point += point; // 여러 번 칭찬을 받을 경우 고려해야 함.
        }

        Collections.sort(nodes, (a, b) -> a.parent - b.parent); // 부모 인덱스 순으로 오름차순 정렬

        for (Node node : nodes) {
            if (node.idx == -1 || node.parent == -1) {
                continue;
            }
            answer[node.idx] = node.point + answer[node.parent];
        }

        for (int i = 1; i < N + 1; i++) {
            System.out.print(answer[i] + " ");
        }
    }

    static class Node {
        int idx;
        int parent;
        int point;

        public Node(int idx, int parent) {
            this.idx = idx;
            this.parent = parent;
        }
    }
}
