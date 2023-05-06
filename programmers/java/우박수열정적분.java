package programmers.java;

import java.util.ArrayList;
import java.util.List;

public class 우박수열정적분 {

}

class 우박수열정적분_Solution {

    List<Integer> collatz = new ArrayList<>();
    double[] prefixSum;

    public double[] solution(int k, int[][] ranges) {
        double[] answer = new double[ranges.length];
        createCollatz(k);
        calculateArea();
        int idx = 0;
        for (int[] range : ranges) {
            if (range[0] >= range[1] + collatz.size()) {
                answer[idx++] = -1.0;
            } else {
                answer[idx++] = getRangeArea(range[0], range[1] + collatz.size());
            }
        }
        return answer;
    }

    private void createCollatz(int k) {
        while (k > 1) {
            collatz.add(k);
            if (k % 2 == 0) {
                k /= 2;
            } else {
                k = k * 3 + 1;
            }
        }
        collatz.add(1);
    }

    private void calculateArea() {
        prefixSum = new double[collatz.size()];
        for (int i = 0; i < collatz.size() - 1; i++) {
            int maxY = Math.max(collatz.get(i), collatz.get(i + 1));
            int minY = Math.min(collatz.get(i), collatz.get(i + 1));
            prefixSum[i + 1] = prefixSum[i] + maxY - (maxY - minY) / (double) 2;
        }
    }

    private double getRangeArea(int start, int end) {
        return prefixSum[end - 1] - prefixSum[start];
    }
}