package ShortestPath.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ11779 {
    static int N, M;
    static Map<Integer, List<int[]>> map = new HashMap<>();
    static Map<Integer, List<Integer>> history = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        for (int i = 1; i <= N; i++) {
            map.put(i, new ArrayList<>());
            history.put(i, new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            map.get(a).add(new int[]{b, c});
        }

        st = new StringTokenizer(br.readLine());

        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        solution(start, end);
    }

    private static void solution(int start, int end) {
        PriorityQueue<int[]> queue = new PriorityQueue<>((x, y) -> x[0] - y[0]);
        int[] dist = new int[N + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;
        queue.add(new int[]{0, start});

        while (!queue.isEmpty()) {
            int[] poll = queue.poll();

            if (poll[0] > dist[poll[1]]) {
                continue;
            }

            for (int[] value : map.get(poll[1])) {
                int next = value[0];
                int cost = value[1];

                if (dist[next] > dist[poll[1]] + cost) {
                    dist[next] = dist[poll[1]] + cost;
                    queue.add(new int[]{dist[next], next});
                    // history 갱신
                    List<Integer> nowHistory = new ArrayList<>();
                    nowHistory.addAll(history.get(poll[1]));
                    nowHistory.add(poll[1]);
                    history.put(next, nowHistory);
                }
            }
        }
        System.out.println(dist[end]);
        System.out.println(history.get(end).size() + 1);
        for (int node : history.get(end)) {
            System.out.print(node + " ");
        }
        System.out.println(end);
    }
}
