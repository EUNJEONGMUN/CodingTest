package Implementation.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ17406 {
    static int N, M, K;
    static int[][] arr;
    static List<int[]> turnPositions = new ArrayList<>();
    static int[] orders;
    static boolean[] visited;
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        arr = new int[N + 1][M + 1];
        orders = new int[K];
        visited = new boolean[K];

        for (int i = 1; i < N + 1; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j < M + 1; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            turnPositions.add(new int[]{Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())});
        }

        permutations(0);
        System.out.println(answer);

    }

    private static void permutations(int idx) {
        if (idx == K) {
            solution();
            return;
        }

        for (int i = 0; i < K; i++) {
            if (visited[i]) {
                continue;
            }
            visited[i] = true;
            orders[idx] = i;
            permutations(idx + 1);
            visited[i] = false;
        }


    }

    private static void solution() {
        int[][] originArr = duplicateArr();
        for (int order : orders) {
            int r = turnPositions.get(order)[0];
            int c = turnPositions.get(order)[1];
            int s = turnPositions.get(order)[2];
            turn(r, c, s, originArr);
        }
        getMinimumRowSum(originArr);
    }

    private static void turn(int r, int c, int s, int[][] originArr) {
        int startR = r - s;
        int startC = c - s;
        int endR = r + s;
        int endC = c + s;

        while (startR < endR && startC < endC) {
            int temp = originArr[startR][startC];

            // ↑
            for (int i = startR; i < endR; i++) {
                originArr[i][startC] = originArr[i + 1][startC];
            }

            // ←
            for (int i = startC; i < endC; i++) {
                originArr[endR][i] = originArr[endR][i + 1];
            }

            // ↓
            for (int i = endR; i > startR; i--) {
                originArr[i][endC] = originArr[i - 1][endC];
            }
            //→
            for (int i = endC; i > startC; i--) {
                originArr[startR][i] = originArr[startR][i - 1];
            }
            originArr[startR][startC + 1] = temp;
            startR++;
            startC++;
            endR--;
            endC--;
        }
    }

    private static void getMinimumRowSum(int[][] newArr) {
        for (int i = 1; i < N + 1; i++) {
            int sum = 0;
            for (int j = 1; j < M + 1; j++) {
                sum += newArr[i][j];
            }
            answer = Math.min(answer, sum);
        }
    }

    private static int[][] duplicateArr() {
        int[][] newArr = new int[N + 1][M + 1];
        for (int i = 1; i < N + 1; i++) {
            for (int j = 1; j < M + 1; j++) {
                newArr[i][j] = arr[i][j];
            }
        }
        return newArr;
    }
}
