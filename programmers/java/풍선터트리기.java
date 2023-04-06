package programmers.java;

import java.util.Arrays;

public class 풍선터트리기 {

    public static void main(String[] args) {
        풍선터트리기_Solution solution = new 풍선터트리기_Solution();
        int[] input = {-16,27,65,-2,58,-92,-71,-68,-61,-33};
        System.out.println(solution.solution(input));
    }
}
class 풍선터트리기_Solution {
    public int solution(int[] a) {
        boolean[] possible = new boolean[a.length];
        Arrays.fill(possible, false);
        int minValue = a[0];
        possible[0] = true;
        for (int i=0; i<possible.length; i++) {
            if (a[i] < minValue) {
                minValue = a[i];
                possible[i] = true;
            }
        }
        minValue = a[a.length-1];
        possible[a.length-1] = true;
        for (int i=possible.length-1; i>-1; i--) {
            if (a[i] < minValue) {
                minValue = a[i];
                possible[i] = true;
            }
        }
        int answer = 0;
        for (boolean p : possible) {
            if (p) answer++;
        }
        return answer;
    }
}
