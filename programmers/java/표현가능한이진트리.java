package programmers.java;

import java.util.Arrays;

public class 표현가능한이진트리 {

    public static void main(String[] args) {
        표현가능한이진트리_Solution solution = new 표현가능한이진트리_Solution();
        long[] input = {7, 42, 5, 63, 111, 95, 129}; // 1, 1, 0, 1, 1, 0, 0
        int[] answer = solution.solution(input);
        System.out.println(Arrays.toString(answer));
    }
}

class 표현가능한이진트리_Solution {

    public int[] solution(long[] numbers) {
        int[] answer = new int[numbers.length];
        Arrays.fill(answer, 0);
        for (int i = 0; i < numbers.length; i++) {
            String binary = Long.toBinaryString(numbers[i]);
            String perfectBinary = makePerfectBinaryTree(binary); // 포화 이진트리로 만들기
            if (search(perfectBinary)) {
                answer[i] = 1;
            }
        }
        return answer;
    }

    private String makePerfectBinaryTree(String binary) {
        int num = 1;
        int digit = 1;
        while (num < binary.length()) {
            num += (Math.pow(2, digit++));
        }
        return "0".repeat(num - binary.length()) + binary;
    }

    private boolean search(String binary) {
        if (binary.length() == 1) {
            return true;
        }
        int rootIdx = binary.length() / 2;
        if (binary.charAt(rootIdx) == '1') {
            boolean left = search(binary.substring(0, rootIdx)); // 왼쪽 서브트리 탐색
            boolean right = search(binary.substring(rootIdx + 1)); // 오른쪽 서브트리 탐색
            return left && right;
        } else {
            if (binary.contains("1")) { // 0인 노드 밑에는 다른 노드가 존재할 수 없다.
                return false;
            }
            return true;
        }
    }
}