package GraphTraversal.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ17070 {
    static int N;
    static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new int[N][N];
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int answer = 0;

        if (board[N - 1][N - 1] == 1) {
            System.out.println(answer);
        } else {


            Queue<Pipe> queue = new LinkedList<>();

            queue.offer(new Pipe(0, 1));

            while (!queue.isEmpty()) {
                Pipe now = queue.poll();
                int headX = now.head / N;
                int headY = now.head % N;

                int tailX = now.tail / N;
                int tailY = now.tail % N;

                if (tailX == N - 1 && tailY == N - 1) {
                    answer++;
                    continue;
                }

                if (headX == tailX) {
                    // 가로
                    if (tailY + 1 < N) {
                        if (tailX + 1 < N) {
                            // 대각선도 가능
                            if (canGo(tailX + 1, tailY + 1) && canGo(tailX, tailY + 1) && canGo(tailX + 1, tailY)) {
                                queue.offer(new Pipe(convert(tailX, tailY), convert(tailX + 1, tailY + 1)));
                            }
                        }
                        if (canGo(tailX, tailY + 1)) {
                            queue.offer(new Pipe(convert(tailX, tailY), convert(tailX, tailY + 1)));
                        }
                    }
                } else if (headY == tailY) {
                    // 세로
                    if (tailX + 1 < N) {
                        if (tailY + 1 < N) {
                            // 대각선도 가능
                            if (canGo(tailX + 1, tailY + 1) && canGo(tailX, tailY + 1) && canGo(tailX + 1, tailY)) {
                                queue.offer(new Pipe(convert(tailX, tailY), convert(tailX + 1, tailY + 1)));
                            }
                        }
                        if (canGo(tailX + 1, tailY)) {
                            queue.offer(new Pipe(convert(tailX, tailY), convert(tailX + 1, tailY)));
                        }
                    }
                } else {
                    // 대각선
                    if (tailX + 1 < N) {
                        if (tailY + 1 < N) {
                            // 대각선도 가능
                            if (canGo(tailX + 1, tailY + 1) && canGo(tailX, tailY + 1) && canGo(tailX + 1, tailY)) {
                                queue.offer(new Pipe(convert(tailX, tailY), convert(tailX + 1, tailY + 1)));
                            }
                        }
                        if (canGo(tailX + 1, tailY)) {
                            queue.offer(new Pipe(convert(tailX, tailY), convert(tailX + 1, tailY)));
                        }
                    }
                    if (tailY + 1 < N) {
                        if (canGo(tailX, tailY + 1)) {
                            queue.offer(new Pipe(convert(tailX, tailY), convert(tailX, tailY + 1)));
                        }
                    }
                }

            }
            System.out.println(answer);
        }
    }

    static class Pipe {
        int head;
        int tail;

        public Pipe(int head, int tail) {
            this.head = head;
            this.tail = tail;
        }
    }

    static int convert(int x, int y) {
        return x * N + y;
    }

    static boolean canGo(int x, int y) {
        if (board[x][y] == 1) {
            return false;
        }
        return true;
    }
}
