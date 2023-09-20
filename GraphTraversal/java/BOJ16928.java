package GraphTraversal.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ16928 {
    static int N, M;
    static Map<Integer, Integer> ladder = new HashMap<>();
    static Map<Integer, Integer> snake = new HashMap<>();
    static boolean[] visited = new boolean[101];
    static Queue<int[]> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            ladder.put(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            snake.put(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        System.out.println(solution());
    }

    private static int solution() {
        visited[1] = true;
        queue.offer(new int[]{1, 0});
        int res;
        while (!queue.isEmpty()) {
            int[] poll = queue.poll();
            res = play(poll[0], poll[1]);
            if (res != -1) {
                return res;
            }
        }

        return -1;
    }

    private static int play(int now, int count) {

        for (int num : List.of(1, 2, 3, 4, 5, 6)) {
            if (now + num == 100) {
                return count + 1;
            }

            if (ladder.containsKey(now + num)) {
                visited[ladder.get(now + num)] = true;
                queue.offer(new int[]{ladder.get(now + num), count + 1});
            } else if (snake.containsKey(now + num)) {
                visited[snake.get(now + num)] = true;
                queue.offer(new int[]{snake.get(now + num), count + 1});
            } else if (!visited[now + num]) {
                visited[now + num] = true;
                queue.offer(new int[]{now + num, count + 1});
            }
        }
        return -1;
    }
}
