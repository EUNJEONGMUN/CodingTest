package Simulation.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ19236 {
    static int[] dx = new int[]{-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dy = new int[]{0, -1, -1, -1, 0, 1, 1, 1};
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        List<Fish> fishes = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 4; j++) {
                int idx = Integer.parseInt(st.nextToken());
                int dir = Integer.parseInt(st.nextToken()) - 1;
                Fish fish = new Fish(idx, dir, i, j, true);
                fishes.add(fish);
            }
        }

        fishes.sort(Fish::compareTo); // 인덱스 순 정렬

        // (0, 0) 물고기 먹고 시작
        Fish fish = findFish(fishes, 0, 0);
        fish.flag = false;
        solution(fishes, 0, 0, fish.dir, fish.idx);
        System.out.println(answer);
    }

    private static void solution(List<Fish> fishes, int sharkX, int sharkY, int sharkDir, int total) {
        moveFish(fishes, sharkX, sharkY);
        for (int i = 1; i < 4; i++) {
            int nx = sharkX + (dx[sharkDir] * i);
            int ny = sharkY + (dy[sharkDir] * i);
            if (!checkRange(nx, ny)) {
                break;
            }
            List<Fish> keepFishes = copyFishes(fishes);
            Fish eatFish = findFish(keepFishes, nx, ny);
            if (eatFish.flag) {
                eatFish.flag = false;
                solution(keepFishes, nx, ny, eatFish.dir, total + eatFish.idx);
                eatFish.flag = true;
            }
        }
        answer = Math.max(answer, total);
    }

    private static List<Fish> copyFishes(List<Fish> fishes) {
        List<Fish> temp = new ArrayList<>();
        for (Fish fish : fishes) {
            temp.add(new Fish(fish.idx, fish.dir, fish.x, fish.y, fish.flag));
        }
        return temp;
    }

    private static void moveFish(List<Fish> fishes, int sharkX, int sharkY) {
        fishes.sort(Fish::compareTo);

        for (int i = 0; i < fishes.size(); i++) {
            Fish fish = fishes.get(i);
            if (!fish.flag) {
                continue;
            }
            int nowX = fish.x;
            int nowY = fish.y;
            int tryCount = 8;
            while (tryCount-- > 0) {
                int nx = nowX + dx[fish.dir];
                int ny = nowY + dy[fish.dir];
                if (checkRange(nx, ny)) {
                    if (sharkX == nx && sharkY == ny) {
                        fish.dir = (fish.dir + 1) % 8;
                        continue;
                    }
                    Fish nextFish = findFish(fishes, nx, ny);
                    fish.swapPosition(nextFish);
                    break;
                }
                fish.dir = (fish.dir + 1) % 8;
            }
        }
    }

    /**
     * fishes 에서 x, y 에 위치한 물고기를 찾아 반환
     */
    private static Fish findFish(List<Fish> fishes, int x, int y) {
        return fishes.stream()
                .filter(f -> f.x == x && f.y == y)
                .findAny()
                .get();
    }

    private static boolean checkRange(int x, int y) {
        return x >= 0 && y >= 0 && x < 4 && y < 4;
    }

    static class Fish implements Comparable<Fish> {
        int idx;
        int dir;
        int x;
        int y;
        boolean flag;

        Fish(int idx, int dir, int x, int y, boolean flag) {
            this.idx = idx;
            this.dir = dir;
            this.x = x;
            this.y = y;
            this.flag = flag;
        }

        /**
         * 두 물고기의 위치를 바꿈.
         */
        private void swapPosition(Fish o) {
            int tempX = o.x;
            int tempY = o.y;
            o.x = this.x;
            o.y = this.y;
            this.x = tempX;
            this.y = tempY;
        }

        @Override
        public int compareTo(Fish o) {
            return this.idx - o.idx;
        }
    }
}
