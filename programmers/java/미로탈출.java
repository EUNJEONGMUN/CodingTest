package programmers.java;

import java.util.*;

public class 미로탈출 {

    public static void main(String[] args) {
        미로탈출_Solution solution = new 미로탈출_Solution();
        int ans = solution.solution(
            new String[]{"SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"});
        System.out.println(ans);
    }
}
class 미로탈출_Solution {

    String[][] matrix;
    int N, M;
    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};

    public int solution(String[] maps) {
        N = maps.length;
        M = maps[0].length();
        matrix = new String[N][M];
        createMatrix(maps);

        int[] startPoint = findMark("S");
        int[] leverPoint = findMark("L");
        int[] endPoint = findMark("E");

        // 시작->레버
        int firstDistance = getShortestDistance(startPoint, leverPoint);
        // 레버->끝
        int secondDistance = getShortestDistance(leverPoint, endPoint);

        if (firstDistance == -1 || secondDistance==-1) {
            return -1;
        }
        return firstDistance+secondDistance;
    }

    private void createMatrix(String[] maps) {
        for (int i=0; i<N; i++){
            String[] split = maps[i].split("");
            for (int j=0; j<M; j++) {
                matrix[i][j] = split[j];
            }
        }
    }

    private boolean checkRange(int x, int y) {
        if (x>=0 && y>=0 && x<N && y<M) {
            return true;
        }
        return false;
    }

    private int[] findMark(String mark) {
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (matrix[i][j].equals(mark)) {
                    return new int[] {i, j};
                }
            }
        }
        return new int[] {-1, -1};
    }

    private int getShortestDistance(int[] startPoint, int[] endPoint) {
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[N][M];
        visited[startPoint[0]][startPoint[1]] = true;
        queue.offer(new int[] {0, startPoint[0], startPoint[1]});

        while(!queue.isEmpty()) {
            int[] now = queue.poll();
            int dist = now[0];
            int x = now[1];
            int y = now[2];

            if (x==endPoint[0] && y==endPoint[1]) {
                return dist;
            }

            for(int i=0; i<4; i++) {
                int nx = x+dx[i];
                int ny = y+dy[i];

                if (checkRange(nx, ny) && !matrix[nx][ny].equals("X") && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    queue.offer(new int[] {dist+1, nx, ny});
                }
            }
        }

        return -1;
    }
}