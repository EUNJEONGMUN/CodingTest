package Backtracking.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class BOJ1987 {
    static int R, C;
    static char[][] arr;
    static boolean[][] visited;
    static int answer;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static Set<Character> history = new HashSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        arr = new char[R][C];
        visited = new boolean[R][C];

        for (int i = 0; i < R; i++) {
            String line = br.readLine().trim();
            for (int j = 0; j < C; j++) {
                arr[i][j] = line.charAt(j);
            }
        }

        visited[0][0] = true;
        history.add(arr[0][0]);
        solution(0, 0, 1);

        System.out.println(answer);


    }

    private static void solution(int x, int y, int count) {
        answer = Math.max(answer, count);

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (checkRange(nx, ny) && !visited[nx][ny] && !history.contains(arr[nx][ny])) {
                visited[nx][ny] = true;
                history.add(arr[nx][ny]);
                solution(nx, ny, count + 1);
                history.remove(arr[nx][ny]);
                visited[nx][ny] = false;
            }
        }
    }

    private static boolean checkRange(int x, int y) {
        return x >= 0 && y >= 0 && x < R && y < C;
    }
}
