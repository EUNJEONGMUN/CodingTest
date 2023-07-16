package Implementation.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ14499 {
    static int N, M, X, Y, K;
    static int[] dx = {0, 0, 0, -1, 1};
    static int[] dy = {0, 1, -1, 0, 0};
    static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());
        Y = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        board = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        Dice dice = new Dice(X, Y);

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < K; i++) {
            int dir = Integer.parseInt(st.nextToken());
            int nx = dice.x + dx[dir];
            int ny = dice.y + dy[dir];
            if (!checkRange(nx, ny)) {
                continue;
            }
            dice.move(nx, ny);
            dice.turn(dir);
            if (board[nx][ny] == 0) {
                board[nx][ny] = dice.down;
            } else {
                dice.down = board[nx][ny];
                board[nx][ny] = 0;
            }

            System.out.println(dice.up);
        }


    }

    private static boolean checkRange(int x, int y) {
        if (x >= 0 && y >= 0 && x < N && y < M) {
            return true;
        }
        return false;
    }
}

class Dice {
    int x;
    int y;
    int up = 0;
    int front = 0;
    int left = 0;
    int right = 0;
    int down = 0;
    int back = 0;

    public Dice(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void move(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void turn(int dir) {
        switch (dir) {
            case 1:
                turn1();
                break;
            case 2:
                turn2();
                break;
            case 3:
                turn3();
                break;
            case 4:
                turn4();
                break;
        }
    }

    private void turn1() {
        int tempUp = up;
        int tempRight = right;
        int tempDown = down;
        int tempLeft = left;

        up = tempRight;
        left = tempUp;
        right = tempDown;
        down = tempLeft;
    }

    private void turn2() {
        int tempUp = up;
        int tempRight = right;
        int tempDown = down;
        int tempLeft = left;

        up = tempLeft;
        left = tempDown;
        right = tempUp;
        down = tempRight;
    }

    private void turn3() {
        int tempBack = back;
        int tempFront = front;
        int tempDown = down;
        int tempUp = up;

        up = tempBack;
        front = tempUp;
        back = tempDown;
        down = tempFront;
    }

    private void turn4() {
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
