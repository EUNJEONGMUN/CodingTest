package programmers.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class 당구연습 {

    public static void main(String[] args) {
        당구연습_Solution solution = new 당구연습_Solution();
        int[][] balls = {{7, 7}, {2, 7}, {7, 3}};
        int[] answer = solution.solution(10, 10, 3, 7, balls);
        System.out.println(Arrays.toString(answer));
    }
}

class 당구연습_Solution {

    int M, N;

    public int[] solution(int m, int n, int startX, int startY, int[][] balls) {
        M = m;
        N = n;
        List<Integer> answer = new ArrayList<>();
        Arrays.stream(balls).forEach(ball -> {
            int ballX = ball[0];
            int ballY = ball[1];
            answer.add(getShortestDistance(startX, startY, ballX, ballY));
        });
        return answer.stream().mapToInt(x -> x).toArray();
    }

    private Integer getShortestDistance(int startX, int startY, int ballX, int ballY) {
        int minValue = Integer.MAX_VALUE;

        // UP
        if (!(ballX == startX && ballY > startY)) {
            minValue = Math.min(minValue, getDistance(ballX, ballY, startX, 2*N-startY));
        }
        // DOWN
        if (!(ballX == startX && ballY < startY)) {
            minValue = Math.min(minValue, getDistance(ballX, ballY, startX, -startY));
        }
        // LEFT
        if (!(ballY == startY && ballX < startX)) {
            minValue = Math.min(minValue, getDistance(ballX, ballY, -startX, startY));
        }
        // RIGHT
        if (!(ballY == startY && ballX > startX)) {
            minValue = Math.min(minValue, getDistance(ballX, ballY, 2*M-startX, startY));
        }
        return minValue;
    }

    private int getDistance(int a, int b, int x, int y) {
        return (int) (Math.pow(a - x, 2) + Math.pow(b - y, 2));
    }
}