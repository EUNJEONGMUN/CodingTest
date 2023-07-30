package GraphTraversal.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ11559 {
    static String[][] board = new String[12][6];
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        for (int i = 0; i < 12; i++) {
            st = new StringTokenizer(br.readLine());
            String[] split = st.nextToken().split("");
            for (int j = 0; j < 6; j++) {
                board[i][j] = split[j];
            }
        }
        int res = 0;
        while (true) {
            if (!solution()) {
                break;
            }
            res++;
        }
        System.out.println(res);
    }

    private static boolean solution() {
        boolean[][] visited = new boolean[12][6];
        boolean flag = false;
        for (int i = 0; i < 12; i++) {
            for (int j = 0; j < 6; j++) {
                if ((!board[i][j].equals(".")) && !visited[i][j]) {
                    if (bfs(i, j, visited)) {
                        flag = true;
                    }
                    ;
                }
            }
        }
        return flag;
    }

    private static boolean bfs(int x, int y, boolean[][] visited) {
        List<int[]> stack = new ArrayList<>();
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});
        stack.add(new int[]{x, y});
        visited[x][y] = true;

        while (!queue.isEmpty()) {
            int[] now = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nx = now[0] + dx[i];
                int ny = now[1] + dy[i];

                if (nx >= 0 && nx < 12 && ny >= 0 && ny < 6 && !visited[nx][ny] && board[x][y].equals(board[nx][ny])) {
                    visited[nx][ny] = true;
                    queue.add(new int[]{nx, ny});
                    stack.add(new int[]{nx, ny});
                }
            }
        }

        if (stack.size() >= 4) {
            boom(stack);
            return true;
        }
        return false;
    }

    private static void boom(List<int[]> stack) {
        for (int i = 0; i < stack.size(); i++) {
            int x = stack.get(i)[0];
            int y = stack.get(i)[1];
            for (int k = x; k > 0; k--) {
                board[k][y] = board[k - 1][y];
            }
            board[0][y] = ".";
        }
    }
}
