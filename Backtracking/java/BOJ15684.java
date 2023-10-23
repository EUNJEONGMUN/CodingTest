package Backtracking.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ15684 {
    static int N, M, H;
    static int[][] arr;
    static int answer = 4;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        arr = new int[H][N - 1];
        for (int[] ints : arr) {
            Arrays.fill(ints, -1);
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            arr[a][b] = 1;
        }

        if (checkAnswer()) {
            System.out.println(0);
        } else {
            solution(0, 0);
            if (answer == 4) {
                answer = -1;
            }
            System.out.println(answer);
        }
    }

    private static void solution(int idx, int count) {
        if (count >= 3 || idx >= (N - 1) * H) {
            return;
        }

        int x = idx / (N - 1);
        int y = idx % (N - 1);

        if (check(x, y)) {
            arr[x][y] = 1;

            if (checkAnswer()) {
                answer = Math.min(answer, count + 1);
            }

            solution(idx + 1, count + 1);
            arr[x][y] = -1;
        }
        solution(idx + 1, count);
    }

    private static boolean check(int x, int y) {
        if (arr[x][y] == 1 || y >= N || x >= H) {
            return false;
        }
        if (y > 0) { // 왼쪽 체크
            if (arr[x][y - 1] == 1) {
                return false;
            }
        }
        if (y < N - 2) { // 오른쪽 체크
            if (arr[x][y + 1] == 1) {
                return false;
            }
        }
        return true;
    }

    private static boolean checkAnswer() {
        for (int i = 0; i < N; i++) {
            if (i != gogo(i)) {
                return false;
            }
        }
        return true;
    }

    private static int gogo(int idx) {
        int col = idx;
        for (int h = 0; h < H; h++) {
            if (col < N - 1 && arr[h][col] == 1) {
                col++;
            } else if (col > 0 && arr[h][col - 1] == 1) {
                col--;
            }
        }
        return col;
    }
}
