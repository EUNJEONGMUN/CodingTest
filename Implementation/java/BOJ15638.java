package Implementation.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ15638 {
    static int N, M;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int[][] board;
    static List<CCTV> one = new ArrayList<>();
    static List<CCTV> two = new ArrayList<>();
    static List<CCTV> three = new ArrayList<>();
    static List<CCTV> four = new ArrayList<>();
    static List<CCTV> five = new ArrayList<>();
    static List<int[]> position = new ArrayList<>();
    static int res = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        board = new int[N][M];
        makeCCTV();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] != 0 && board[i][j] < 6) {
                    position.add(new int[]{i, j, board[i][j]});
                }
            }
        }

        bt(0);
        System.out.println(res);
    }

    private static int countSpace() {
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == 0) {
                    cnt++;
                }
            }
        }
        return cnt;
    }

    private static void bt(int idx) {
        if (idx == position.size()) {
            res = Math.min(res, countSpace());
            return;
        }

        int x = position.get(idx)[0];
        int y = position.get(idx)[1];
        int type = position.get(idx)[2];

        List<CCTV> nowCCTV = new ArrayList<>();
        switch (type) {
            case 1:
                nowCCTV = one;
                break;
            case 2:
                nowCCTV = two;
                break;
            case 3:
                nowCCTV = three;
                break;
            case 4:
                nowCCTV = four;
                break;
            case 5:
                nowCCTV = five;
                break;
        }
        for (CCTV cctv : nowCCTV) {
            Queue<int[]> q = new LinkedList<>();
            for (int dir : cctv.canSeeDir) {
                int nx = x;
                int ny = y;
                while (checkRange(nx + dx[dir], ny + dy[dir]) && board[nx + dx[dir]][ny + dy[dir]] < 6) {
                    if (board[nx + dx[dir]][ny + dy[dir]] == 0) {
                        q.add(new int[]{nx + dx[dir], ny + dy[dir]});
                    }
                    board[nx + dx[dir]][ny + dy[dir]] = type;
                    nx += dx[dir];
                    ny += dy[dir];
                }
            }
            bt(idx + 1);
            while (!q.isEmpty()) {
                int[] p = q.poll();
                board[p[0]][p[1]] = 0;
            }
        }
    }


    private static void makeCCTV() {
        for (int i = 0; i < 4; i++) {
            one.add(new CCTV(1, new int[]{i}));
        }

        two.add(new CCTV(2, new int[]{0, 2}));
        two.add(new CCTV(2, new int[]{1, 3}));


        three.add(new CCTV(3, new int[]{0, 1}));
        three.add(new CCTV(3, new int[]{1, 2}));
        three.add(new CCTV(3, new int[]{2, 3}));
        three.add(new CCTV(3, new int[]{3, 0}));

        four.add(new CCTV(4, new int[]{0, 1, 2}));
        four.add(new CCTV(4, new int[]{0, 1, 3}));
        four.add(new CCTV(4, new int[]{0, 2, 3}));
        four.add(new CCTV(4, new int[]{1, 2, 3}));

        five.add(new CCTV(5, new int[]{0, 1, 2, 3}));
    }

    private static boolean checkRange(int x, int y) {
        if (x >= 0 && y >= 0 && x < N && y < M) {
            return true;
        }
        return false;
    }

    private static class CCTV {
        int type;
        int[] canSeeDir;

        public CCTV(int type, int[] canSeeDir) {
            this.type = type;
            this.canSeeDir = canSeeDir;
        }
    }
}
