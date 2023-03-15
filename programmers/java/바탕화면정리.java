package programmers.java;

import java.util.Arrays;

public class 바탕화면정리 {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String[] str_arr = {"..", "#."};
        int[] ans = solution.solution(str_arr);
        System.out.println(Arrays.toString(ans));
    }
}

class Solution {

    public int[] solution(String[] wallpaper) {
        int min_x = wallpaper.length, min_y = wallpaper[0].length(), max_x = 0, max_y = 0;

        for (int i = 0; i < wallpaper.length; i++) {
            for (int j = 0; j < wallpaper[i].length(); j++) {
                if (wallpaper[i].charAt(j) == '#') {
                    min_x = Math.min(i, min_x);
                    min_y = Math.min(j, min_y);
                    max_x = Math.max(i, max_x);
                    max_y = Math.max(j, max_y);
                }
            }
        }
        int[] answer = {min_x, min_y, max_x+1, max_y+1};
        return answer;
    }
}