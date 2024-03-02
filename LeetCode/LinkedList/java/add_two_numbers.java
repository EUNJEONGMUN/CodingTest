package LeetCode.LinkedList.java;
/*
https://leetcode.com/problems/add-two-numbers/?envType=study-plan-v2&envId=top-interview-150
 */

import java.util.List;

public class add_two_numbers {
    public static void main(String[] args) {
        Solution solution = new Solution();
        solution.addTwoNumbers(ListNode.createList(List.of(2, 4, 3)), ListNode.createList(List.of(5, 6, 4)));
    }
}

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode answer = new ListNode(0);
        ListNode now = answer;
        ListNode A = l1;
        ListNode B = l2;
        while (A != null || B != null || now.val > 0) {
            int remain;
            if (now.val == -1) {
                remain = 0;
            } else {
                remain = now.val;
            }
            if (A != null) {
                remain += A.val;
                A = A.next;
            }

            if (B != null) {
                remain += B.val;
                B = B.next;
            }

            now.val = remain % 10;
            now.next = new ListNode(remain / 10);
            now = now.next;
        }
        return answer;
    }

}

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    public static ListNode createList(List<Integer> arr) {
        ListNode ret = new ListNode();
        ListNode now = ret;
        for (int i = 0; i < arr.size(); i++) {
            now.val = arr.get(i);
            if (i != arr.size() - 1) {
                now.next = new ListNode();
                now = now.next;
            }
        }
        return ret;
    }

    @Override
    public String toString() {
        return "val:" + val + "\n";
    }
}