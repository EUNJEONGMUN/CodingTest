package GraphTraversal.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ17182 {
    static int N, K;
    static int[][] board;
    static int answer = Integer.MAX_VALUE;
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        board = new int[N][N];
        visited = new boolean[N];

        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int k=0; k<N; k++) {
            for(int i=0; i<N; i++) {
                for(int j=0; j<N; j++) {
                    if (i==j) {
                        continue;
                    }
                    board[i][j] = Math.min(board[i][j], board[i][k]+board[k][j]);
                }
            }
        }

        visited[K] = true;
        bt(1, K, 0);

        if (answer == Integer.MAX_VALUE) {
            System.out.println(0);
        } else {
            System.out.println(answer);
        }

    }

    static void bt(int visitedCount, int nowNode, int cost) {

        if (visitedCount == N) {
            answer = Math.min(cost, answer);
            return;
        }

        for (int j=0; j<N; j++) {
            if (board[nowNode][j] == 0 || visited[j]) {
                continue;
            }
            visited[j] = true;
            bt(visitedCount+1, j, cost+board[nowNode][j]);
            visited[j] = false;
        }
    }
}
