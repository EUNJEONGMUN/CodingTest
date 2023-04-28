package programmers.java;

public class 연속된부분수열의합 {

    public static void main(String[] args) {
        연속된부분수열의합_Solution solution = new 연속된부분수열의합_Solution();
        int[] ans = solution.solution(new int[]{1, 2, 3, 4, 5}, 7);
    }
}

class 연속된부분수열의합_Solution {

    int total;
    int left = 0;
    int right = -1;

    public int[] solution(int[] sequence, int k) {
        int minLength = sequence.length + 1;
        int answerLeft = 0;
        int answerRight = 0;

        while (right < sequence.length) {
            if (total == k) {
                if ((right - left + 1) < minLength) {
                    minLength = right - left + 1;
                    answerLeft = left;
                    answerRight = right;
                }
                total -= sequence[left++];
            } else if (total > k) {
                total -= sequence[left++];
            } else if (total < k) {
                if (right + 1 < sequence.length) {
                    total += sequence[++right];
                }
            }

        }
        int[] answer = {answerLeft, answerRight};
        return answer;
    }
}