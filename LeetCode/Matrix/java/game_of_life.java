package LeetCode.Matrix.java;
/*
https://leetcode.com/problems/game-of-life/?envType=study-plan-v2&envId=top-interview-150
 */
public class game_of_life {
    static int[][] count;
    static int M, N;
    static int[] dx = {-1, -1, -1, 0, 1, 1, 1, 0};
    static int[] dy = {-1, 0, 1, 1, 1, 0, -1, -1};

    public void gameOfLife(int[][] board) {
        M = board.length;
        N = board[0].length;
        count = new int[M][N];

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == 1) {
                    addCount(i, j);
                }
            }
        }

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == 1 && count[i][j] < 2) {
                    board[i][j] = 0;
                } else if (board[i][j] == 1 && count[i][j] > 3) {
                    board[i][j] = 0;
                } else if (board[i][j] == 0 && count[i][j] == 3) {
                    board[i][j] = 1;
                }
            }
        }

    }

    private void addCount(int x, int y) {
        int nx, ny;
        for (int dir = 0; dir < 8; dir++) {
            nx = x + dx[dir];
            ny = y + dy[dir];
            if (checkRange(nx, ny)) {
                count[nx][ny]++;
            }
        }
    }

    private boolean checkRange(int x, int y) {
        return x >= 0 && y >= 0 && x < M && y < N;
    }
}
