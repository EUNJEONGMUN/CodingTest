package LeetCode.TwoPointers.java;

import java.util.Arrays;

/*
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150
 */
public class two_sum_ii_input_array_is_sorted {
    public static void main(String[] args) {
        int[] answer = twoSum(new int[]{2, 7, 11, 15}, 9);
        System.out.println(Arrays.toString(answer)); // [1, 2]
    }

    public static int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;
        int[] answer = new int[2];

        while (left < right) {
            if (numbers[left] + numbers[right] == target) {
                answer[0] = left + 1;
                answer[1] = right + 1;
                break;
            }
            if (numbers[left] + numbers[right] < target) {
                left++;
            } else {
                right--;
            }
        }
        return answer;
    }
}
