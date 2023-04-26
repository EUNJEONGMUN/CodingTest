package programmers.java;

import java.util.Arrays;

public class 요격시스템 {

    public static void main(String[] args) {
        요격시스템_Solution solution = new 요격시스템_Solution();
        int ans = solution.solution(
            new int[][]{{4, 5}, {4, 8}, {10, 14}, {11, 13}, {5, 12}, {3, 7}, {1, 4}});
        System.out.println(ans);

    }

}

class 요격시스템_Solution {

    public int solution(int[][] targets) {
        Arrays.sort(targets, (o1, o2) -> {
            return Integer.compare(o1[1], o2[1]);
        });
        int answer = 0;
        int time = targets[0][1];
        for (int[] target : targets) {
            if (time <= target[0]) {
                answer++;
                time = target[1];
            }
        }
        answer++;
        return answer;
    }
}