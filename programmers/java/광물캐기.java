package programmers.java;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


public class 광물캐기 {

    public static void main(String[] args) {
        광물캐기_Solution solution = new 광물캐기_Solution();
        int ans = solution.solution(new int[]{1, 3, 2},
            new String[]{"diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron",
                "stone"});
        int ans2 = solution.solution(new int[]{0, 1, 1},
            new String[]{"diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron",
                "iron", "iron", "iron", "diamond"});
        System.out.println(ans);
        System.out.println(ans2);
    }

}

class 광물캐기_Solution {

    public int solution(int[] picks, String[] minerals) {

        // 1. 5개씩 끊어서 다이아몬드, 철, 돌의 개수를 센다. 곡괭이를 다 쓰면 더이상 캘 수 없다.
        List<int[]> fiveMinerals = new ArrayList<>();
        int pickCount = 0;
        int mineralIdx = 0;
        while (pickCount<picks[0]+picks[1]+picks[2] && mineralIdx<minerals.length) {
            int diamond = 0;
            int iron = 0;
            int stone = 0;
            for (int i = mineralIdx; i < Math.min(mineralIdx + 5, minerals.length); i++) {
                if (minerals[i].equals("diamond")) {
                    diamond++;
                } else if (minerals[i].equals("iron")) {
                    iron++;
                } else if (minerals[i].equals("stone")) {
                    stone++;
                }
            }
            fiveMinerals.add(new int[]{diamond, iron, stone});
            pickCount++;
            mineralIdx += 5;

        }

        // 2. 다이아몬드, 철, 돌의 개수 순서대로 내림차순 정렬한다.
        Collections.sort(fiveMinerals, ((o1, o2) -> {
            if (o1[0] == o2[0]) {
                if (o1[1] == o2[1]) {
                    return Integer.compare(o2[2], o1[2]);
                }
                return Integer.compare(o2[1], o1[1]);
            }
            return Integer.compare(o2[0], o1[0]);
        }));

        // 3. 다이아몬드, 철, 돌의 곡괭이순으로 계산한다.
        int answer = 0;
        int pickIdx = 0;
        int groupIdx = 0;
        while (pickIdx < picks.length && groupIdx < fiveMinerals.size()) {
            if (picks[pickIdx] == 0) {
                pickIdx++;
                continue;
            }
            if (pickIdx == 0) {
                answer += (fiveMinerals.get(groupIdx)[0] + fiveMinerals.get(groupIdx)[1] + fiveMinerals.get(
                    groupIdx)[2]);
            } else if (pickIdx == 1) {
                answer += (fiveMinerals.get(groupIdx)[0] * 5 + fiveMinerals.get(groupIdx)[1] + fiveMinerals.get(
                    groupIdx)[2]);
            } else if (pickIdx == 2) {
                answer += (fiveMinerals.get(groupIdx)[0] * 25 + fiveMinerals.get(groupIdx)[1] * 5
                    + fiveMinerals.get(groupIdx)[2]);
            }
            picks[pickIdx]--;
            groupIdx++;
        }
        return answer;
    }
}