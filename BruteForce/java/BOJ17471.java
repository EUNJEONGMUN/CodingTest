package BruteForce.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ17471 {
    static int N;
    static int[] people;
    static int[][] arr;
    static boolean[] visited;
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        people = new int[N];
        arr = new int[N][N];
        visited = new boolean[N];
        for (int[] ints : arr) {
            Arrays.fill(ints, 0);
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            people[i] = Integer.parseInt(st.nextToken());
        }

        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            for (int j=0; j<m; j++) {
                int k = Integer.parseInt(st.nextToken())-1;
                arr[i][k] = 1;
            }
        }

        solution(0);

        if (answer == Integer.MAX_VALUE) {
            System.out.println(-1);
        } else {
            System.out.println(answer);
        }
    }

    private static void solution(int idx) {
        if (idx == N) {
            if (check(true) && check(false)) { // visited와 notVisited가 각각 연결 되어 있는 지 확인
                int sumA = 0, sumB = 0;
                for (int i=0; i<N; i++) {
                    if (visited[i]) {
                        sumA += people[i];
                    } else {
                        sumB += people[i];
                    }
                }
                if (Math.abs(sumA-sumB) < answer) {
                    answer = Math.abs(sumA-sumB);
                }
            }
            return;
        }

        visited[idx] = true; // 방문할 때
        solution(idx+1);
        visited[idx] = false; // 방문하지 않을 때
        solution(idx+1);
    }

    private static boolean check(boolean mark) {

        Set<Integer> checkSet = new HashSet<>();
        for(int i=0; i<N; i++) {
            if (visited[i] == mark) {
                checkSet.add(i);
            }
        }

        if (checkSet.size() < 1) {
            return false;
        } else if (checkSet.size() == 1) {
            return true;
        }

        for(int i=0; i<N; i++) {
            if (visited[i] == mark) {
                Queue<Integer> queue = new LinkedList<>();
                queue.offer(i);

                while (!queue.isEmpty()) {
                    Integer node = queue.poll();

                    for (int j=0; j<N; j++) {
                        if (arr[node][j] == 1 && visited[j] == mark && checkSet.contains(j)) {
                            checkSet.remove(j);
                            queue.offer(j);
                        }
                    }
                }
                break;
            }
        }

        return checkSet.isEmpty();
    }
}
