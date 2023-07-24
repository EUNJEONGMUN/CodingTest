package Simulation.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ15683 {
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        List<Gear> gears = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            gears.add(new Gear(br.readLine()));
        }
        N = Integer.parseInt(br.readLine());

        StringTokenizer st;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int index = Integer.parseInt(st.nextToken()) - 1;
            int dir = Integer.parseInt(st.nextToken());

            int[] isTurn = new int[gears.size()];
            Arrays.fill(isTurn, 0);

            int now = index;
            isTurn[now] = dir;

            while (now > 0) {
                if (gears.get(now).arr.get(6) == gears.get(now - 1).arr.get(2)) {
                    break;
                }
                isTurn[now - 1] = isTurn[now] * (-1);
                now--;
            }

            now = index;
            while (now < gears.size() - 1) {
                if (gears.get(now).arr.get(2) == gears.get(now + 1).arr.get(6)) {
                    break;
                }
                isTurn[now + 1] = isTurn[now] * (-1);
                now++;
            }
            for (int g=0; g<gears.size(); g++) {
                if (isTurn[g]==-1) {
                    gears.get(g).turnAnticlockwise();
                } else if (isTurn[g]==1) {
                    gears.get(g).turnClockwise();
                }
            }
        }

        int res = 0;
        if (gears.get(0).arr.get(0) == 1) {
            res += 1;
        }
        if (gears.get(1).arr.get(0) == 1) {
            res += 2;
        }
        if (gears.get(2).arr.get(0) == 1) {
            res += 4;
        }
        if (gears.get(3).arr.get(0) == 1) {
            res += 8;
        }
        System.out.println(res);
    }

    private static class Gear {
        List<Integer> arr = new ArrayList<>();

        public Gear(String temp) {
            String[] split = temp.split("");
            for (String s : split) {
                arr.add(Integer.parseInt(s));
            }
        }

        public void turnClockwise() {
            int temp = arr.remove(arr.size() - 1);
            arr.add(0, temp);
        }

        public void turnAnticlockwise() {
            int temp = arr.remove(0);
            arr.add(temp);
        }
    }
}
