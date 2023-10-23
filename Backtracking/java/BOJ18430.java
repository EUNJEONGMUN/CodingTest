package Backtracking.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ18430 {
    static int N, M, res;
    static int[][] arr;
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        solution(0, 0);
        System.out.println(res);
    }

    private static void solution(int index, int temp) {
        if (index == N * M) {
            res = Math.max(temp, res);
            return;
        }

        int x = index / M;
        int y = index % M;

        if (!visited[x][y]) {

            if ((y + 1 < M && !visited[x][y + 1]) && (x + 1 < N && !visited[x + 1][y])) {
                visited[x][y] = true;
                visited[x][y + 1] = true;
                visited[x + 1][y] = true;
                solution(index + 1, temp + (arr[x][y] * 2) + arr[x][y + 1] + arr[x + 1][y]);
                visited[x][y] = false;
                visited[x][y + 1] = false;
                visited[x + 1][y] = false;
            }


            if ((y - 1 >= 0 && !visited[x][y - 1]) && (x + 1 < N && !visited[x + 1][y])) {
                visited[x][y] = true;
                visited[x][y - 1] = true;
                visited[x + 1][y] = true;
                solution(index + 1, temp + (arr[x][y] * 2) + arr[x][y - 1] + arr[x + 1][y]);
                visited[x][y] = false;
                visited[x][y - 1] = false;
                visited[x + 1][y] = false;
            }

            if ((y - 1 >= 0 && !visited[x][y - 1]) && (x - 1 >= 0 && !visited[x - 1][y])) {
                visited[x][y] = true;
                visited[x][y - 1] = true;
                visited[x - 1][y] = true;
                solution(index + 1, temp + (arr[x][y] * 2) + arr[x][y - 1] + arr[x - 1][y]);
                visited[x][y] = false;
                visited[x][y - 1] = false;
                visited[x - 1][y] = false;
            }

            if ((y + 1 < M && !visited[x][y + 1]) && (x - 1 >= 0 && !visited[x - 1][y])) {
                visited[x][y] = true;
                visited[x][y + 1] = true;
                visited[x - 1][y] = true;
                solution(index + 1, temp + (arr[x][y] * 2) + arr[x][y + 1] + arr[x - 1][y]);
                visited[x][y] = false;
                visited[x][y + 1] = false;
                visited[x - 1][y] = false;
            }
        }
        solution(index + 1, temp);
    }
}