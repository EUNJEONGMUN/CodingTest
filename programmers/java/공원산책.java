package programmers.java;

import java.util.Arrays;

public class 공원산책 {

    public static void main(String[] args) {
        공원산책_Solution solution = new 공원산책_Solution();
        int[] ans = solution.solution(new String[]{"SOO", "OXX", "OOO"},
            new String[]{"E 2", "S 2", "W 1"});
        System.out.println(Arrays.toString(ans));
    }
}

class 공원산책_Solution {

    int[] dx = {-1, 1, 0, 0}; // N, S, W, E
    int[] dy = {0, 0, -1, 1};
    int N, M;
    String[][] matrix;
    int[] position;

    public int[] solution(String[] park, String[] routes) {
        N = park.length;
        M = park[0].length();
        matrix = new String[N][M];
        init(park);
        position = findStartPoint();

        for (String route : routes) {
            String[] split = route.split(" ");
            int dir = findDir(split[0]);
            int cnt = Integer.parseInt(split[1]);

            if (canGo(dir, cnt)) {
                position[0] += dx[dir]*cnt;
                position[1] += dy[dir]*cnt;
            }
        }

        return position;
    }

    private void init(String[] park) {
        for (int i = 0; i < N; i++) {
            String[] split = park[i].split("");
            for (int j = 0; j < M; j++) {
                matrix[i][j] = split[j];
            }
        }
    }

    private int[] findStartPoint() {
        int[] startPoint = new int[2];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (matrix[i][j].equals("S")) {
                    startPoint[0] = i;
                    startPoint[1] = j;
                }
            }
        }
        return startPoint;
    }

    private boolean checkRange(int x, int y) {
        if (x >= 0 && x < N && y >= 0 && y < M) {
            return true;
        }
        return false;
    }

    private int findDir(String op) {
        if (op.equals("N")) {
            return 0;
        } else if (op.equals("S")) {
            return 1;
        } else if (op.equals("W")) {
            return 2;
        }
        return 3;
    }

    private boolean canGo(int dir, int cnt) {
        int nx = position[0];
        int ny = position[1];

        for (int i=0; i<cnt; i++) {
            nx += dx[dir];
            ny += dy[dir];
            if (!checkRange(nx, ny) || matrix[nx][ny].equals("X")) {
                return false;
            }
        }
        return true;
    }
}