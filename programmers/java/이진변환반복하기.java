package programmers.java;

import java.util.Arrays;

public class 이진변환반복하기 {

    public static void main(String[] args) {
        이진변환반복하기_Solution solution = new 이진변환반복하기_Solution();
        int[] ans = solution.solution("110010101001");
        System.out.println(Arrays.toString(ans));
        ans = solution.solution("01110");
        System.out.println(Arrays.toString(ans));
        ans = solution.solution("1111111");
        System.out.println(Arrays.toString(ans));
    }
}

class 이진변환반복하기_Solution {

    public int[] solution(String s) {
        int count = 0;
        int total_count = 0;
        while (true) {
            int zero_count = (int) s.chars().filter(e -> e == '0').count();
            if (s.equals("1")) {
                break;
            }
            s = Integer.toBinaryString(s.length() - zero_count);
            total_count += zero_count;
            count++;
        }
        int[] answer = {count, total_count};
        return answer;
    }
}
