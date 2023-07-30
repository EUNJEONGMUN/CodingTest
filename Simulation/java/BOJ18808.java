package Simulation.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ18808 {
    static int N, M, K;
    static int[][] graphPaper;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        graphPaper = new int[N][M];
        for (int i=0; i<K; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            String[] stickerInput = new String[n];
            for (int j=0; j<n; j++) {
                stickerInput[j] = br.readLine();
            }
            Sticker sticker = new Sticker(n, m, stickerInput);
            int cnt = 0;
            while (cnt<4) {
                if (findPosition(sticker)) {
                    printGraphPaper();
                    break;
                }
                sticker.turn();
                cnt++;
            }
        }
        System.out.println(calculate());

    }

    private static void printGraphPaper() {
        System.out.println("------------------");
        for (int j=0; j<N; j++) {
            System.out.println(Arrays.toString(graphPaper[j]));
        }
    }

    private static boolean findPosition(Sticker sticker) {
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (canPutOn(i, j, sticker)) {
                    putOn(i, j, sticker);
                    return true;
                }
            }
        }
        return false;
    }

    private static void putOn(int x, int y, Sticker sticker) {
        int n = sticker.arr.length;
        int m = sticker.arr[0].length;

        for (int i=x; i<x+n; i++) {
            for (int j=y; j<y+m; j++) {
                if (sticker.arr[i-x][j-y] == 1) {
                    graphPaper[i][j] = 1;
                }
            }
        }
    }

    private static int calculate() {
        int res = 0;
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                res += graphPaper[i][j];
            }
        }
        return res;
    }

    private static boolean canPutOn(int x, int y, Sticker sticker) {
        int n = sticker.arr.length;
        int m = sticker.arr[0].length;

        if (x+n <= N && y+m <= M) {
            for (int i=x; i<x+n; i++) {
                for (int j=y; j<y+m; j++) {
                    if (graphPaper[i][j] == 1 && sticker.arr[i-x][j-y] == 1) {
                        return false;
                    }
                }
            }
            return true;
        }
        return false;
    }

    static class Sticker {
        int[][] arr;

        public Sticker(int n, int m, String[] arr) {
            this.arr = new int[n][m];
            for (int i=0; i<arr.length; i++) {
                String[] split = arr[i].split(" ");
                for (int j = 0; j < split.length; j++) {
                    this.arr[i][j] = Integer.parseInt(split[j]);
                }
            }
        }

        public void turn() {
            int n = arr.length;
            int m = arr[0].length;
            int[][] newArr = new int[m][n];
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    newArr[i][j] = this.arr[n - 1 - j][i];
                }
            }
            this.arr = newArr;
        }
    }
}
