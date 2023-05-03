package programmers.java;

import java.util.LinkedList;
import java.util.Queue;

public class 카카오프렌즈컬러링북 {

}

class 카카오프렌즈컬러링북_Solution {

    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};
    boolean[][] visited;
    int N, M;

    public int[] solution(int n, int m, int[][] picture) {
        N = n;
        M = m;
        visited = new boolean[N][M];

        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (picture[i][j] != 0 && !visited[i][j]) {
                    maxSizeOfOneArea = Math.max(bfs(i, j, picture[i][j], picture),
                        maxSizeOfOneArea);
                    numberOfArea++;
                }
            }
        }
        int[] answer = {numberOfArea, maxSizeOfOneArea};
        return answer;
    }

    private int bfs(int x, int y, int mark, int[][] picture) {
        Queue<int[]> queue = new LinkedList<>();
        visited[x][y] = true;
        queue.offer(new int[]{x, y});
        int cnt = 1;
        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = now[0] + dx[i];
                int ny = now[1] + dy[i];

                if (checkRange(nx, ny) && picture[nx][ny] == mark && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    queue.offer(new int[]{nx, ny});
                    cnt++;
                }
            }
        }
        return cnt;
    }

    private boolean checkRange(int x, int y) {
        if (x >= 0 && y >= 0 && x < N && y < M) {
            return true;
        }
        return false;
    }
}