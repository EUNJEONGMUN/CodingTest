package programmers.java;

import java.util.LinkedList;
import java.util.Objects;
import java.util.Queue;

public class 리코쳇로봇 {

    public static void main(String[] args) {
        리코쳇로봇_Solution solution = new 리코쳇로봇_Solution();
        String[] board = {".D.R", "....", ".G..", "...D"};
        int ans = solution.solution(board);
        System.out.println(ans);
    }


}

class 리코쳇로봇_Solution {

    int[] dx = {0, 0, -1, 1};
    int[] dy = {-1, 1, 0, 0};

    int N, M;

    public int solution(String[] board) {
        N = board.length;
        M = board[0].length();
        Position start = new Position(0, 0, 0);
        Position end = new Position(0, 0, 0);
        boolean[][] visited = new boolean[N][M];
        int answer = -1;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i].charAt(j) == 'R') {
                    start = new Position(i, j, 0);
                    visited[i][j] = true;
                }
                if (board[i].charAt(j) == 'G') {
                    end = new Position(i, j, 0);
                }
            }
        }
        Queue<Position> queue = new LinkedList<>();
        queue.offer(start);

        while (!queue.isEmpty()) {
            Position now = queue.poll();
            if (now.equals(end)) {
                answer = now.dist;
                break;
            }
            for (int i = 0; i < 4; i++) {
                int nx = now.x;
                int ny = now.y;
                while (checkRange(nx + dx[i], ny + dy[i])
                    && board[nx + dx[i]].charAt(ny + dy[i]) != 'D') {
                    nx = nx + dx[i];
                    ny = ny + dy[i];
                }
                if ((nx == now.x && ny == now.y) || visited[nx][ny]) {
                    continue;
                }
                queue.offer(new Position(nx, ny, now.dist + 1));
                visited[nx][ny] = true;
            }
        }
        return answer;
    }

    private boolean checkRange(int x, int y) {
        if (x >= 0 && y >= 0 && x < N && y < M) {
            return true;
        }
        return false;
    }

    class Position {

        int x;
        int y;
        int dist;

        Position(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }

        public int hashCode() {
            return Objects.hash(x, y);
        }

        public boolean equals(Object obj) {
            if (!(obj instanceof Position)) {
                return false;
            }
            Position o = (Position) obj;
            if (o.x == this.x && o.y == this.y) {
                return true;
            }
            return false;
        }
    }
}