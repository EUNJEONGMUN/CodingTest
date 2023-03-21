package programmers.java;

import java.util.ArrayDeque;
import java.util.Deque;

public class 보행자천국 {

    public static void main(String[] args) {
        보행자천국_Solution solution = new 보행자천국_Solution();
        int[][] map = {{0, 2, 0, 0, 0, 2}, {0, 0, 2, 0, 1, 0}, {1, 0, 0, 2, 2, 0}};
        int ans = solution.solution(3, 6, map);
        System.out.println(ans);
    }
}

class 보행자천국_Solution {

    int MOD = 20170805;
    int M, N;

    public int solution(int m, int n, int[][] cityMap) {
        M = m;
        N = n;
        Count[][] cnt = new Count[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cnt[i][j] = new Count(0, 0);
            }
        }
        boolean[][] visited = new boolean[m][n];

        Deque<Position> queue = new ArrayDeque<>();
        queue.add(new Position(1, 0));
        queue.add(new Position(0, 1));
        visited[0][0] = true;
        cnt[0][0] = new Count(0, 0);

        while (!queue.isEmpty()) {
            Position p = queue.pop();

            if (p.checkRange() && !visited[p.x][p.y]) {
                Position up = new Position(p.x - 1, p.y);
                Position left = new Position(p.x, p.y - 1);
                int leftCnt = 0;
                int upCnt = 0;
                if (up.checkRange()) {
                    if (cityMap[up.x][up.y] == 0) {
                        upCnt += cnt[up.x][up.y].sum();
                    } else if (cityMap[up.x][up.y] == 2) {
                        upCnt += cnt[up.x][up.y].up;
                    }
                    if (up.x == 0 && up.y == 0) {
                        upCnt++;
                    }

                }
                if (left.checkRange()) {
                    if (cityMap[left.x][left.y] == 0) {
                        leftCnt += cnt[left.x][left.y].sum();
                    } else if (cityMap[left.x][left.y] == 2) {
                        leftCnt += cnt[left.x][left.y].left;
                    }
                    if (left.x == 0 && left.y == 0) {
                        leftCnt++;
                    }
                }

                cnt[p.x][p.y] = new Count(leftCnt, upCnt);
                visited[p.x][p.y] = true;
                queue.add(new Position(p.x + 1, p.y));
                queue.add(new Position(p.x, p.y + 1));
            }
        }

        return cnt[m - 1][n - 1].sum();
    }


    class Position {

        int x;
        int y;

        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }

        private boolean checkRange() {
            if (this.x >= 0 && this.y >= 0 && this.x < M && this.y < N) {
                return true;
            }
            return false;
        }
    }

    class Count {

        int left;
        int up;

        public Count(int left, int up) {
            this.left = left % MOD;
            this.up = up % MOD;
        }

        public int sum() {
            return (left + up) % MOD;
        }
    }
}