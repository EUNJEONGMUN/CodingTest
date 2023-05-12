package programmers.java;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class 경주로건설 {

    public static void main(String[] args) {
        경주로건설_Solution solution = new 경주로건설_Solution();
        int ans = solution.solution(new int[][]{{0, 0, 0, 0, 0, 0, 0, 1}, {0, 0, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0, 1, 0, 0}, {0, 0, 0, 0, 1, 0, 0, 0},
            {0, 0, 0, 1, 0, 0, 0, 1}, {0, 0, 1, 0, 0, 0, 1, 0}, {0, 1, 0, 0, 0, 1, 0, 0},
            {1, 0, 0, 0, 0, 0, 0, 0}});
        System.out.println(ans);
    }
}

class 경주로건설_Solution {

    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};
    int N;
    int[][][] cost;

    public int solution(int[][] board) {
        N = board.length;
        cost = new int[N][N][4];
        init();

        Queue<int[]> queue = new LinkedList<>(); // 비용, x, y, 방향;
        queue.offer(new int[]{0, 0, 0, -1});
        Arrays.fill(cost[0][0], 0);

        while (!queue.isEmpty()) {
            int[] now = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nx = now[1] + dx[i];
                int ny = now[2] + dy[i];

                if (checkRange(nx, ny) && board[nx][ny] == 0) {
                    if (now[3] == i || now[3] == -1) {
                        // 전과 방향이 같을 때, 혹은 처음일 때
                        if (cost[nx][ny][i] >= now[0] + 1) {
                            queue.offer(new int[]{now[0] + 1, nx, ny, i});
                            cost[nx][ny][i] = now[0] + 1;
                        }
                    } else {
                        if (cost[nx][ny][i] >= now[0] + 6) {
                            queue.offer(new int[]{now[0] + 6, nx, ny, i});
                            cost[nx][ny][i] = now[0] + 6;
                        }
                    }
                }
            }
        }
        return Math.min(Math.min(cost[N - 1][N - 1][0], cost[N - 1][N - 1][1]),
            Math.min(cost[N - 1][N - 1][2], cost[N - 1][N - 1][3])) * 100;

    }

    private void init() {
        for (int[][] co : cost) {
            for (int[] c : co) {
                Arrays.fill(c, Integer.MAX_VALUE);
            }
        }
    }

    private boolean checkRange(int x, int y) {
        if (x >= 0 && y >= 0 && x < N && y < N) {
            return true;
        }
        return false;
    }
}