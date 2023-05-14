package GraphTraversal.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ14466 {
    static int N, K, R;
    static int[][] cows;
    static Map<Position, List> bridges = new HashMap<>();

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        cows = new int[N + 1][N + 1];

        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            Position start = new Position(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            Position end = new Position(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            if (!bridges.containsKey(start)) {
                bridges.put(start, new ArrayList());
            }
            if (!bridges.containsKey(end)) {
                bridges.put(end, new ArrayList());
            }
            bridges.get(start).add(end);
            bridges.get(end).add(start);
        }

        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            cows[x][y] = 1;
        }

        checkPair();
        System.out.println(answer / 2);
    }

    private static void checkPair() {
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (cows[i][j] == 1) {
                    bfs(new Position(i, j));
                }
            }
        }
    }

    private static void bfs(Position position) {
        boolean[][] visited = new boolean[N + 1][N + 1];
        Queue<Position> queue = new LinkedList<>();
        int cnt = -1;
        queue.add(position);
        visited[position.x][position.y] = true;

        while (!queue.isEmpty()) {
            Position now = queue.poll();
            if (cows[now.x][now.y] == 1) {
                cnt++;
            }

            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];

                if (checkRange(nx, ny) && visited[nx][ny] == false) {
                    if (bridges.containsKey(now) && bridges.get(now).contains(new Position(nx, ny))) {
                        continue;
                    }
                    queue.add(new Position(nx, ny));
                    visited[nx][ny] = true;
                }

            }
        }
        answer += (K - cnt - 1);
    }

    private static boolean checkRange(int x, int y) {
        if (x > 0 && y > 0 && x <= N && y <= N) {
            return true;
        }
        return false;
    }

    static class Position {
        int x;
        int y;

        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }

        @Override
        public boolean equals(Object obj) {
            if (!(obj instanceof Position)) {
                return false;
            }
            Position p = (Position) obj;
            return p.x == this.x && p.y == this.y;
        }

        @Override
        public String toString() {
            return "[" + this.x + " " + this.y + "]";
        }
    }
}
