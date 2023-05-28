package GraphTraversal.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ2638 {
    static int N, M;
    static int[][] board;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int cheeseCount = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 1) {
                    cheeseCount++;
                }

            }
        }
        int time = 0;
        while (cheeseCount != 0) {
            int[][] count = new int[N][M];
            boolean[][] visited = new boolean[N][M];
            Queue<int[]> queue = new LinkedList<>();

            // 초기 빈칸 큐에 삽입
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (board[i][j] == 0) {
                        queue.offer(new int[]{i, j});
                        visited[i][j] = true;
                        break;
                    }
                }
                if (!queue.isEmpty()) {
                    break;
                }
            }

            while (!(queue.isEmpty())) {
                int[] now = queue.poll();

                for (int i = 0; i < 4; i++) {
                    int nx = now[0] + dx[i];
                    int ny = now[1] + dy[i];

                    if (checkRange(nx, ny)) {
                        if (board[nx][ny] == 1) {
                            count[nx][ny]++;
                            continue;
                        }
                        if (visited[nx][ny] == false) {
                            visited[nx][ny] = true;
                            queue.offer(new int[]{nx, ny});
                        }
                    }
                }
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (count[i][j] > 1) {
                        board[i][j] = 0;
                        cheeseCount--;
                    }
                }
            }
            time++;
        }
        System.out.println(time);
    }

    private static boolean checkRange(int x, int y) {
        if (x >= 0 && y >= 0 && x < N && y < M) {
            return true;
        }
        return false;
    }
}
