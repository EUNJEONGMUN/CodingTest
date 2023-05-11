package programmers.java;

import java.util.ArrayDeque;
import java.util.Deque;

public class 게임맵최단거리 {

    public static void main(String[] args) {
        게임맵최단거리_Solution solution = new 게임맵최단거리_Solution();
        int[][] value = {{1, 0, 1, 1, 1}, {1, 0, 1, 0, 1}, {1, 0, 1, 1, 1},{1, 1, 1, 0, 1},{0, 0, 0, 0, 1}};
        int ans = solution.solution(value);
        System.out.println(ans);
    }

}

class 게임맵최단거리_Solution {

    static int N, M;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int[][] distance;

    public int solution(int[][] maps) {
        N = maps.length;
        M = maps[0].length;
        distance = new int[N][M];
        init();

        Deque<Position> queue = new ArrayDeque<>();
        distance[0][0] = 1;
        queue.offer(new Position(1, 0, 0));

        while (!queue.isEmpty()) {
            Position p = queue.poll();
            if (p.dist > distance[p.x][p.y]) {
                continue;
            }

            for (int i = 0; i < 4; i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];

                if (checkRange(nx, ny) && maps[nx][ny] != 0) {
                    if (p.dist + 1 < distance[nx][ny]) {
                        distance[nx][ny] = p.dist + 1;
                        queue.offer(new Position(p.dist + 1, nx, ny));
                    }
                }
            }
        }

        if (distance[N - 1][M - 1] == Integer.MAX_VALUE) {
            return -1;
        }
        return distance[N - 1][M - 1];
    }

    private boolean checkRange(int nx, int ny) {
        if (nx >= 0 && ny >= 0 && nx < N && ny < M) {
            return true;
        }
        return false;
    }

    private void init() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                distance[i][j] = Integer.MAX_VALUE;
            }
        }
    }

    class Position {

        int dist;
        int x;
        int y;

        public Position(int dist, int x, int y) {
            this.dist = dist;
            this.x = x;
            this.y = y;
        }
    }
}