package programmers.java;

public class 최소직사각형 {

    public static void main(String[] args) {
        int[][] arr = {{60, 50}, {30, 70}, {60, 30}, {4, 20}, {80, 40}};
        최소직사각형_Solution solution = new 최소직사각형_Solution();
        int ans = solution.solution(arr);
        System.out.println(ans);
    }
}

class 최소직사각형_Solution {

    public int solution(int[][] sizes) {
        int width = 0;
        int height = 0;

        for (int[] size : sizes) {
            width = Math.max(width, Math.min(size[0], size[1]));
            height = Math.max(height, Math.max(size[0], size[1]));
        }
        return width * height;
    }
}