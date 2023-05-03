package programmers.java;

public class 연속펄스부분수열의합 {

}

class 연속펄스부분수열의합_Solution {

    public long solution(int[] sequence) {
        int[] pulse1 = new int[sequence.length];
        int[] pulse2 = new int[sequence.length];

        for (int i = 0; i < sequence.length; i++) {
            if (i % 2 == 0) {
                pulse1[i] = sequence[i];
                pulse2[i] = sequence[i] * (-1);

            } else {
                pulse1[i] = sequence[i] * (-1);
                pulse2[i] = sequence[i];
            }
        }
        return Math.max(getMaxValue(pulse1), getMaxValue(pulse2));
    }

    private long getMaxValue(int[] arr) {
        long maxValue = Long.MIN_VALUE;
        long value = 0;
        for (int end = 0; end < arr.length; end++) {
            if (value + arr[end] < 0) {
                maxValue = Math.max(value, maxValue);
                value = 0;
            } else {
                value += arr[end];
                maxValue = Math.max(value, maxValue);
            }
        }
        return maxValue;
    }
}