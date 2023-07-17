package GraphTraversal.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ17141 {
    static int N, M;
    static int[][] laboratory;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};
    static List<int[]> virus;
    static List<int[]> pickVirusPosition = new ArrayList<>();
    static int answer = -1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        laboratory = new int[N][N];

        virus = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                laboratory[i][j] = Integer.parseInt(st.nextToken());
                if (laboratory[i][j] == 2) {
                    virus.add(new int[]{i, j});
                }
            }
        }

        solution(0, M);
        System.out.println(answer);

    }

    private static void solution(int idx, int cnt) {
        if (cnt == 0) {
            int ans = bfs();
            if (ans != -1) {
                if (answer == -1) {
                    answer = ans;
                } else {
                    answer = Math.min(answer, ans);
                }
            }
            return;
        }
        for (int i = idx; i < virus.size(); i++) {
            pickVirusPosition.add(virus.get(i));
            solution(i + 1, cnt - 1);
            pickVirusPosition.remove(pickVirusPosition.size() - 1);
        }
    }

    private static int bfs() {

        int[][] board = new int[N][N];

        for (int i = 0; i < N; i++) {
            Arrays.fill(board[i], -1);
        }

        for (int[] p : pickVirusPosition) {
            board[p[0]][p[1]] = 0;
        }

        Queue<int[]> queue = new LinkedList<>();

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == 0) {
                    queue.add(new int[]{i, j});
                }
            }
        }

        while (!queue.isEmpty()) {
            int[] now = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nx = now[0] + dx[i];
                int ny = now[1] + dy[i];

                if (checkRange(nx, ny) && laboratory[nx][ny] != 1 && board[nx][ny] == -1) {
                    board[nx][ny] = board[now[0]][now[1]] + 1;
                    queue.add(new int[]{nx, ny});
                }
            }
        }

        int res = 0;

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == -1 && laboratory[i][j] != 1) {
                    return -1;
                }
                res = Math.max(res, board[i][j]);
            }
        }

        return res;
    }

    private static boolean checkRange(int x, int y) {
        if (x >= 0 && y >= 0 && x < N && y < N) {
            return true;
        }
        return false;
    }
}
