package BruteForce.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_18428 {

    static String[][] board;
    static String answer = "NO";
    static int N;
    //    static int[] log = new int[3];
    static List<int[]> teachers = new ArrayList<>();
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new String[N][N];

        StringTokenizer st;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < N; j++) {
                board[i][j] = st.nextToken();
                if (board[i][j].equals("T")) {
                    teachers.add(new int[]{i, j});
                }
            }
        }

        combi(0, 0);
        System.out.println(answer);

    }

    private static void combi(int depth, int idx) {
        if (depth == 3) {
            if (check()) {
                answer = "YES";
            }
            return;
        }

        for (int i = idx; i < N * N; i++) {
            if (board[i / N][i % N].equals("S") || board[i / N][i % N].equals("T")) {
                continue;
            }
//            log[depth] = i;
            board[i / N][i % N] = "O";
            combi(depth + 1, i + 1);
            board[i / N][i % N] = "X";
        }
    }

    private static boolean check() {
        for (int[] teacher : teachers) {
            int x = teacher[0];
            int y = teacher[1];
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                while (checkRange(nx, ny)) {
                    if (board[nx][ny].equals("S")) {
                        return false;
                    }
                    if (board[nx][ny].equals("O")) {
                        break;
                    }
                    nx += dx[i];
                    ny += dy[i];
                }
            }
        }
        return true;
    }

    private static boolean checkRange(int x, int y) {
        if (x >= 0 && x < N && y >= 0 && y < N) {
            return true;
        }
        return false;
    }
}


