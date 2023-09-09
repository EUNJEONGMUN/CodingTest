package Implementation.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ14890 {
    static int N, L;
    static int[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        arr = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int answer = 0;
        for (int i = 0; i < N; i++) {
            answer += searchCol(i) ? 1 : 0;
            answer += searchRow(i) ? 1 : 0;
        }
        System.out.println(answer);
    }

    private static boolean searchCol(int y) {
        boolean[] mark = new boolean[N];
        int height = arr[0][y];
        int count = 1;
        for (int x = 1; x < N; x++) {
            if (Math.abs(arr[x][y] - height) > 1) {
                return false;
            }
            if (arr[x][y] == height) {
                count++;
                continue;
            }
            if (arr[x][y] < height) {
                count = 1;
                height = arr[x][y];
            } else {
                if (count < L) {
                    return false;
                } else {
                    for (int idx = x - 1; idx > x - L - 1; idx--) {
                        if (mark[idx]) {
                            return false;
                        }
                        mark[idx] = true;
                    }
                    count = 1;
                    height = arr[x][y];
                }
            }
        }

        height = arr[N - 1][y];
        count = 1;
        for (int x = N - 2; x >= 0; x--) {
            if (Math.abs(arr[x][y] - height) > 1) {
                return false;
            }
            if (arr[x][y] == height) {
                count++;
                continue;
            }
            if (arr[x][y] < height) {
                count = 1;
                height = arr[x][y];
            } else {
                if (count < L) {
                    return false;
                } else {
                    for (int idx = x + 1; idx < x + L + 1; idx++) {
                        if (mark[idx]) {
                            return false;
                        }
                        mark[idx] = true;
                    }
                    count = 1;
                    height = arr[x][y];
                }
            }
        }
        return true;
    }


    private static boolean searchRow(int x) {
        boolean[] mark = new boolean[N];
        int height = arr[x][0];
        int count = 1;
        for (int y = 1; y < N; y++) {
            if (Math.abs(arr[x][y] - height) > 1) {
                return false;
            }
            if (arr[x][y] == height) {
                count++;
                continue;
            }
            if (arr[x][y] < height) {
                count = 1;
                height = arr[x][y];
            } else {
                if (count < L) {
                    return false;
                } else {
                    for (int idx = y - 1; idx > y - L - 1; idx--) {
                        if (mark[idx]) {
                            return false;
                        }
                        mark[idx] = true;
                    }
                    count = 1;
                    height = arr[x][y];
                }
            }
        }

        height = arr[x][N - 1];
        count = 1;
        for (int y = N - 2; y >= 0; y--) {
            if (Math.abs(arr[x][y] - height) > 1) {
                return false;
            }
            if (arr[x][y] == height) {
                count++;
                continue;
            }
            if (arr[x][y] < height) {
                count = 1;
                height = arr[x][y];
            } else {
                if (count < L) {
                    return false;
                } else {
                    for (int idx = y + 1; idx < y + L + 1; idx++) {
                        if (mark[idx]) {
                            return false;
                        }
                        mark[idx] = true;
                    }
                    count = 1;
                    height = arr[x][y];
                }
            }
        }
        return true;
    }
}
