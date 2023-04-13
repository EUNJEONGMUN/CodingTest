package GraphTraversal.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ17142 {

    static int N, M;
    static int[][] board;
    static List<Virus> virus = new ArrayList<>();
    static int[] log;
    static boolean[][] visited;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};
    static int answer = Integer.MAX_VALUE;
    static int empty = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][N];
        log = new int[M];

        for (int i = 0; i < N; i++) {
            String[] split = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(split[j]);
                if (board[i][j] == 2) {
                    virus.add(new Virus(i, j));
                } else if (board[i][j] == 0) {
                    empty++;
                }
            }
        }

        if (empty == 0) {
            System.out.println(0);
        } else {
            combi(0, 0);
            if (answer == Integer.MAX_VALUE) {
                System.out.println(-1);
            } else {
                System.out.println(answer);
            }
        }
    }

    private static void combi(int idx, int depth) {
        if (depth == log.length) {
            int res = bfs(empty);
            if (res != -1) {
                answer = Math.min(bfs(empty), answer);
            }
            return;
        }

        for (int i = idx; i < virus.size(); i++) {
            log[depth] = i;
            combi(i + 1, depth + 1);
        }
    }

    private static int bfs(int emptySpace) {
        Queue<Node> queue = new LinkedList<>();
        visited = new boolean[N][N];
        for (int i : log) {
            Virus p = virus.get(i);
            queue.offer(new Node(0, p));
            visited[p.x][p.y] = true;
        }

        while (!queue.isEmpty()) {
            Node node = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nx = node.virus.x + dx[i];
                int ny = node.virus.y + dy[i];
                if (checkRange(nx, ny) && board[nx][ny] != 1 && !visited[nx][ny]) {
                    if (board[nx][ny] == 0) {
                        emptySpace--;
                    }
                    if (emptySpace == 0) {
                        return node.second+1;
                    }
                    visited[nx][ny] = true;
                    queue.offer(new Node(node.second + 1, new Virus(nx, ny)));
                }
            }
        }
        return -1;
    }

    private static boolean checkRange(int x, int y) {
        if (x >= 0 && y >= 0 && x < N && y < N) {
            return true;
        }
        return false;
    }

    static class Node {

        int second;
        Virus virus;

        public Node(int second, Virus virus) {
            this.second = second;
            this.virus = virus;
        }
    }

    static class Virus {

        int x;
        int y;

        public Virus(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

}
