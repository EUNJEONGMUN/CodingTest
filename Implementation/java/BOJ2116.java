package Implementation.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ2116 {
    static int N;
    static List<Dice> diceList = new ArrayList<>();
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            diceList.add(new Dice(st));
        }

        for (int bottomNum : List.of(1, 2, 3, 4, 5, 6)) {
            diceList.get(0).setBottomIdx(bottomNum);

            for (int i = 1; i < N; i++) {
                diceList.get(i).setBottomIdx(diceList.get(i - 1).getTopNum());
            }

            answer = Math.max(answer, diceList.stream()
                    .map(dice -> dice.getLargestNum())
                    .reduce(0, Integer::sum));
        }
        System.out.println(answer);
    }

    static class Dice {
        static int[] top = new int[]{5, 3, 4, 1, 2, 0};
        int[] dice = new int[6];
        int bottomIdx;

        public Dice(StringTokenizer st) {
            for (int i = 0; i < 6; i++) {
                dice[i] = Integer.parseInt(st.nextToken());
            }
        }

        public void setBottomIdx(int bottom) {
            for (int i = 0; i < 6; i++) {
                if (dice[i] == bottom) {
                    bottomIdx = i;
                }
            }
        }

        public int getTopNum() {
            return dice[top[bottomIdx]];
        }

        public int getLargestNum() {
            int res = 0;
            for (int i = 0; i < 6; i++) {
                if (i == bottomIdx || i == top[bottomIdx]) {
                    continue;
                }
                res = Math.max(res, dice[i]);
            }
            return res;
        }
    }
}
