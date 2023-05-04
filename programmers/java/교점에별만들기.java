package programmers.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class 교점에별만들기 {

    public static void main(String[] args) {
        교점에별만들기_Solution solution = new 교점에별만들기_Solution();
        String[] ans = solution.solution(
            new int[][]{{2, -1, 4}, {-2, -1, 4}, {0, -1, 1}, {5, -8, -12}, {5, 8, 12}});
        System.out.println(Arrays.toString(ans));

    }
}

class 교점에별만들기_Solution {

    public String[] solution(int[][] line) {
        List<long[]> points = new ArrayList<>();
        long minX = Long.MAX_VALUE;
        long minY = Long.MAX_VALUE;
        long maxX = Long.MIN_VALUE;
        long maxY = Long.MIN_VALUE;

        for (int i = 0; i < line.length - 1; i++) {
            for (int j = i + 1; j < line.length; j++) {
                if (line[i][0] * line[j][1] - line[i][1] * line[j][0] == 0) {
                    continue;
                }
                double[] cross = getCross(line[i], line[j]);
                if (isInteger(cross)) {
                    points.add(new long[]{(long) cross[0], (long) cross[1]});
                    minX = Math.min(minX, (long) cross[0]);
                    minY = Math.min(minY, (long) cross[1]);
                    maxX = Math.max(maxX, (long) cross[0]);
                    maxY = Math.max(maxY, (long) cross[1]);
                }
            }
        }

        boolean[][] arr = new boolean[(int) (maxY - minY + 1)][(int) (maxX - minX + 1)];
        for (long[] point : points) {
            arr[(int) (maxY - point[1])][(int) (point[0] - minX)] = true;
        }

        String[] answer = new String[arr.length];

        for (int i = 0; i < arr.length; i++) {
            StringBuilder sb = new StringBuilder();
            for (boolean check : arr[i]) {
                if (check) {
                    sb.append("*");
                } else {
                    sb.append(".");
                }
            }
            answer[i] = sb.toString();
        }
        return answer;
    }

    private double[] getCross(int[] line1, int[] line2) {
        long A = line1[0];
        long B = line1[1];
        long E = line1[2];
        long C = line2[0];
        long D = line2[1];
        long F = line2[2];
        double x = (double) (B * F - E * D) / (A * D - B * C);
        double y = (double) (E * C - A * F) / (A * D - B * C);
        return new double[]{x, y};
    }

    private boolean isInteger(double[] cross) {
        if (cross[0] % 1 == 0.0 && cross[1] % 1 == 0.0) {
            return true;
        }
        return false;
    }
}
