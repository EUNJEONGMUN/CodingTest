package programmers.java;

import java.util.*;

public class 석유시추 {
    static int N, M;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static boolean[][] visited;
    static int[] total;

    public static void main(String[] args) {
        int[][] land1 = {{0, 0, 0, 1, 1, 1, 0, 0}, {0, 0, 0, 0, 1, 1, 0, 0}, {1, 1, 0, 0, 0, 1, 1, 0}, {1, 1, 1, 0, 0, 0, 0, 0}, {1, 1, 1, 0, 0, 0, 1, 1}};
        System.out.println(solution(land1)); //9
        int[][] land2 = {{1, 0, 1, 0, 1, 1}, {1, 0, 1, 0, 0, 0}, {1, 0, 1, 0, 0, 1}, {1, 0, 0, 1, 0, 0}, {1, 0, 0, 1, 0, 1}, {1, 0, 0, 0, 0, 0}, {1, 1, 1, 1, 1, 1}};
        System.out.println(solution(land2)); // 16
    }

    public static int solution(int[][] land) {
        N = land.length;
        M = land[0].length;
        visited = new boolean[N][M];
        total = new int[M];
        Arrays.fill(total, 0);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (land[i][j] == 1 && !visited[i][j]) {
                    Result res = search(i, j, land);
                    sumResult(res);
                }
            }
        }
        Arrays.sort(total);
        return total[total.length - 1];
    }

    private static boolean checkRange(int x, int y) {
        return x >= 0 && y >= 0 && x < N && y < M;
    }

    private static void sumResult(Result result) {
        for (Integer col : result.searchList) {
            total[col] += result.total;
        }
    }

    private static Result search(int x, int y, int[][] land) {
        Result result = new Result();
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{x, y});
        result.addSearchList(y);
        visited[x][y] = true;

        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = now[0] + dx[i];
                int ny = now[1] + dy[i];

                if (checkRange(nx, ny) && !visited[nx][ny] && land[nx][ny] == 1) {
                    queue.offer(new int[]{nx, ny});
                    result.addSearchList(ny);
                    visited[nx][ny] = true;
                }
            }
        }

        return result;
    }

    static class Result {
        int total = 0;
        Set<Integer> searchList = new HashSet<>();

        private void addSearchList(int col) {
            total++;
            searchList.add(col);
        }
    }
}