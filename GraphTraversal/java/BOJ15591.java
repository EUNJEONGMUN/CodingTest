package GraphTraversal.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ15591 {
    static int N, Q;
    static List<int[]>[] distance;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        distance = new ArrayList[N + 1];
        for (int i = 0; i < N + 1; i++) {
            distance[i] = new ArrayList<>();
        }

        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            distance[a].add(new int[]{b, c});
            distance[b].add(new int[]{a, c});
        }

        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            System.out.println(solution(v, k));
        }
    }

    private static int solution(int start, int k) {
        boolean[] visited = new boolean[N + 1];
        Arrays.fill(visited, false);
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        visited[start] = true;

        int ans = 0;

        while (!queue.isEmpty()) {
            int poll = queue.poll();
            for (int[] d : distance[poll]) {
                if (!visited[d[0]] && d[1] >= k) { // bfs 탐색하면서 k 보다 클 경우에 추가
                    queue.add(d[0]);
                    visited[d[0]] = true;
                    ans++;
                }
            }
        }
        return ans;
    }
}
