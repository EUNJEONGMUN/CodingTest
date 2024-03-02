package LeetCode.BinarySearch.java;
/*
https://leetcode.com/problems/search-insert-position/?envType=study-plan-v2&envId=top-interview-150
 */

public class search_insert_position {
}
class Solution {
    public int searchInsert(int[] nums, int target) {

        int left = 0;
        int right = nums.length;

        while (left < right) {
            int mid = (left+right)/2;

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[mid] > target) {
                right = mid;
            } else {
                left = mid+1;
            }
        }
        return right;

    }
}
