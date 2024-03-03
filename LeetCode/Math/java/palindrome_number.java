package LeetCode.Math.java;
/*
https://leetcode.com/problems/palindrome-number/?envType=study-plan-v2&envId=top-interview-150
 */

public class palindrome_number {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.isPalindrome(1));
    }
}

class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int originNumber = x;
        int reverseNumber = 0;
        while (x > 0) {
            reverseNumber = reverseNumber * 10 + x % 10;
            x /= 10;
        }
        return originNumber == reverseNumber;
    }
}