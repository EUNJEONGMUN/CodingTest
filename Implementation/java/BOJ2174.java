package Implementation.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ2174 {
    static int A, B, N, M;
    static String[] direction = new String[]{"N", "E", "S", "W"};
    static Map<String, Integer> directionMap = new HashMap<>() {{
        put("N", 0);
        put("E", 1);
        put("S", 2);
        put("W", 3);
    }};
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static List<Robot> robotList = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            String dir = st.nextToken();
            robotList.add(new Robot(x, y, dir));
        }

        boolean flag = false;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int idx = Integer.parseInt(st.nextToken()) - 1;
            String op = st.nextToken();
            int cnt = Integer.parseInt(st.nextToken());

            if (flag) {
                continue;
            }

            Robot now = robotList.get(idx);
            int dir = directionMap.get(now.dir);

            if (op.equals("F")) {
                for (int j = 0; j < cnt; j++) {
                    int nx = now.x + dx[dir];
                    int ny = now.y + dy[dir];
                    int sameIdx = isSamePosition(idx, nx, ny);
                    if (sameIdx != -1) {
                        System.out.println("Robot " + (idx + 1) + " crashes into robot " + (sameIdx + 1));
                        flag = true;
                        break;
                    }
                    if (!checkRange(nx, ny)) {
                        System.out.println("Robot " + (idx + 1) + " crashes into the wall");
                        flag = true;
                        break;
                    }
                    now.x = nx;
                    now.y = ny;
                }

            } else if (op.equals("L")) {
                for (int j = 0; j < cnt; j++) {
                    dir -= 1;
                    if (dir == -1) {
                        dir = 3;
                    }
                }
                now.dir = direction[dir];
            } else if (op.equals("R")) {
                for (int j = 0; j < cnt; j++) {
                    dir += 1;
                    if (dir == 4) {
                        dir = 0;
                    }
                }
                now.dir = direction[dir];
            }
        }
        if (!flag) {
            System.out.println("OK");
        }
    }

    static private int isSamePosition(int idx, int x, int y) {
        for (int i = 0; i < robotList.size(); i++) {
            if (i == idx) {
                continue;
            }
            Robot robot = robotList.get(i);
            if (robot.x == x && robot.y == y) {
                return i;
            }
        }
        return -1;
    }

    static private boolean checkRange(int x, int y) {
        if (x > 0 && y > 0 && x <= A && y <= B) {
            return true;
        }
        return false;
    }

    static class Robot {
        int x;
        int y;
        String dir;

        public Robot(int x, int y, String dir) {
            this.x = x;
            this.y = y;
            this.dir = dir;
        }
    }
}
