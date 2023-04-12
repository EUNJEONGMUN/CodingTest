package programmers.java;

import java.util.LinkedList;
import java.util.Queue;

public class 네트워크 {


}

class 네트워크_Solution {

    boolean[] visited;

    public int solution(int n, int[][] computers) {
        visited = new boolean[n];
        int answer = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                bfs(i, computers);
                answer++;
            }
        }

        return answer;
    }

    private void bfs(int node, int[][] computers) {
        Queue<Integer> queue = new LinkedList<>();
        visited[node] = true;
        queue.offer(node);

        while (!queue.isEmpty()) {
            int now = queue.poll();

            for (int i = 0; i < computers[now].length; i++) {
                if (i == now) {
                    continue;
                }
                if (computers[now][i] == 1) {
                    if (!visited[i]) {
                        visited[i] = true;
                        queue.offer(i);
                    }
                }
            }

        }
    }
}