package Backtracking.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class BOJ1941 {

    static String[][] board = new String[5][5];
    static int[] log = new int[7];
    static int answer = 0;
    static boolean[] visited = new boolean[25];
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 5; i++) {
            String[] split = br.readLine().split("");
            for (int j = 0; j < 5; j++) {
                board[i][j] = split[j];
            }
        }

        dfs(0, 0);
        System.out.println(answer);
    }

    private static void dfs(int depth, int start) {
        if (depth == 7) {
            if (check()) {
                answer++;
            }
            return;
        }

        for (int i = start; i < 25; i++) {
            if (!visited[i]) {
                visited[i] = true;
                log[depth] = i;
                dfs(depth + 1, i + 1);
                visited[i] = false;
            }
        }

    }

    private static boolean check() {
        int cntY = 0;
        for (int i : log) {
            if (board[i / 5][i % 5].equals("Y")) {
                cntY++;
            }
        }
        if (cntY > 3) {
            return false;
        }

        List<Integer> logs = new ArrayList<>();
        for (int i : log) {
            logs.add(i);
        }
        Deque<Integer> q = new ArrayDeque<>();
        q.offer(log[0]);

        while (!q.isEmpty()) {
            int now = q.poll();
            int x = now / 5;
            int y = now % 5;
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                Integer next = nx * 5 + ny;
                if (checkRange(nx, ny) && logs.contains(next)) {
                    q.offer(next);
                    logs.remove(next);
                }
            }
        }
        if (logs.isEmpty()) {
            return true;
        }
        return false;
    }

    private static boolean checkRange(int nx, int ny) {
        if (nx >= 0 && ny >= 0 && nx < 5 && ny < 5) {
            return true;
        }
        return false;
    }
}
