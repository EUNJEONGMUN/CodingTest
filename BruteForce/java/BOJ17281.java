package BruteForce.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ17281 {
    static int N;
    static int answer;
    static int[] orders = new int[9];
    static boolean[] visited = new boolean[9];
    static Map<Integer, List<Integer>> player = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            player.put(i, new ArrayList<>());
            for (int j = 0; j < 9; j++) {
                player.get(i).add(Integer.parseInt(st.nextToken()));
            }
        }
        visited[3] = true;
        orders[3] = 0;
        permutations(1);
        System.out.println(answer);
    }

    public static void permutations(int idx) {
        if (idx == 9) {
            answer = Math.max(answer, solution());
            return;
        }

        for (int i = 0; i < 9; i++) {
            if (visited[i]) {
                continue;
            }

            orders[i] = idx;
            visited[i] = true;
            permutations(idx + 1);
            visited[i] = false;

        }
    }

    private static int solution() {
        int idx = 0;
        int point = 0;
        boolean[] ground;

        for (int round = 0; round < N; round++) {
            int out = 0;
            ground = new boolean[3];
            while (out < 3) {
                int act = player.get(round).get(orders[idx]);
                if (act == 0) {
                    out++;
                } else if (act == 1) {
                    if (ground[2]) {
                        point++;
                        ground[2] = false;
                    }
                    if (ground[1]) {
                        ground[2] = true;
                        ground[1] = false;
                    }
                    if (ground[0]) {
                        ground[1] = true;
                    }
                    ground[0] = true;

                } else if (act == 2) {
                    if (ground[2]) {
                        point++;
                        ground[2] = false;
                    }
                    if (ground[1]) {
                        point++;
                        ground[1] = false;
                    }

                    if (ground[0]) {
                        ground[2] = true;
                        ground[0] = false;
                    }
                    ground[1] = true;

                } else if (act == 3) {
                    for (int i = 0; i < 3; i++) {
                        if (ground[i]) {
                            point++;
                            ground[i] = false;
                        }
                    }
                    ground[2] = true;

                } else if (act == 4) {
                    for (int i = 0; i < 3; i++) {
                        if (ground[i]) {
                            point++;
                            ground[i] = false;
                        }
                    }
                    point++;
                }
                idx = (idx + 1) % 9;
            }
        }

        return point;
    }
}
