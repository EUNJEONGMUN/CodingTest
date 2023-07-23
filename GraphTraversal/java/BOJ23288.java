package GraphTraversal.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ23288 {

    static int N, M, K;
    static int[] dx = {0, 1, 0, -1}; // 동 남 서 북
    static int[] dy = {1, 0, -1, 0};
    static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        board = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int result = 0;
        Dice dice = new Dice();

        for (int i = 0; i < K; i++) {
            dice.move();
            result += getScore(dice.x, dice.y);
            dice.turn(board[dice.x][dice.y]);
        }
        System.out.println(result);

    }

    private static int getScore(int x, int y) {
        final int num = board[x][y];
        boolean[][] visited = new boolean[board.length][board[0].length];
        visited[x][y] = true;
        int count = 1;
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});

        while (!queue.isEmpty()) {
            int[] p = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nx = p[0] + dx[i];
                int ny = p[1] + dy[i];

                if (checkRange(nx, ny) && !visited[nx][ny] && board[nx][ny] == num) {
                    count += 1;
                    visited[nx][ny] = true;
                    queue.add(new int[]{nx, ny});
                }
            }
        }
        return num * count;
    }

    private static boolean checkRange(int x, int y) {
        if (x >= 0 && y >= 0 && x < N && y < M) {
            return true;
        }
        return false;
    }

    static class Dice {
        int dir = 0;
        int x = 0;
        int y = 0;
        int up = 1; // 위
        int front = 5;
        int left = 4;
        int right = 3;
        int down = 6;
        int back = 2;

        public void move() {
            checkDir();
            x += dx[dir];
            y += dy[dir];

            switch (dir) {
                case 0:
                    turn0();
                    break;
                case 1:
                    turn1();
                    break;
                case 2:
                    turn2();
                    break;
                case 3:
                    turn3();
                    break;
            }
        }

        public void turn(int B) {
            if (down > B) {
                turnClockwise();
            } else if (down < B) {
                turnAnticlockwise();
            }
        }

        private void checkDir() {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (!checkRange(nx, ny)) {
                turnReverse();
            }
        }

        public void turnClockwise() {
            dir = (dir + 1) % 4;
        }

        public void turnAnticlockwise() {
            dir = dir - 1;
            if (dir == -1) {
                dir = 3;
            }
        }

        private void turnReverse() {
            dir = (dir + 2) % 4;
        }

        private void turn0() { // 동
            int tempUp = up;
            int tempRight = right;
            int tempDown = down;
            int tempLeft = left;

            up = tempLeft;
            left = tempDown;
            right = tempUp;
            down = tempRight;
        }

        private void turn2() {  //서
            int tempUp = up;
            int tempRight = right;
            int tempDown = down;
            int tempLeft = left;

            up = tempRight;
            left = tempUp;
            right = tempDown;
            down = tempLeft;
        }

        private void turn1() {  //남
            int tempBack = back;
            int tempFront = front;
            int tempDown = down;
            int tempUp = up;

            up = tempBack;
            front = tempUp;
            back = tempDown;
            down = tempFront;
        }

        private void turn3() {  //북
            int tempBack = back;
            int tempFront = front;
            int tempDown = down;
            int tempUp = up;

            up = tempFront;
            front = tempDown;
            back = tempUp;
            down = tempBack;
        }
    }
}

