package LeetCode.Heap.java;

import java.util.Collections;
import java.util.PriorityQueue;

/*
https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=study-plan-v2&envId=top-interview-150
 */
public class kth_largest_element_in_an_array {
}
class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());

        for (int n : nums) {
            queue.offer(n);
        }

        for (int i=1; i<k; i++) {
            queue.poll();
        }
        return queue.poll();

    }
}