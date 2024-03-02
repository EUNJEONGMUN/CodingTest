package LeetCode.KadanesAlgorithm.java;
/*
https://leetcode.com/problems/maximum-subarray/description/?envType=study-plan-v2&envId=top-interview-150
 */

public class maximum_subarray {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.maxSubArray(new int[]{5, 4, -1, 7, 8})); // 23
    }
}

class Solution {
    public int maxSubArray(int[] nums) {
        int answer = -Integer.MAX_VALUE;
        int nowMax = 0;
        for (int num : nums) {
            nowMax = Math.max(nowMax + num, num);
            answer = Math.max(nowMax, answer);
        }

        return answer;
    }
}