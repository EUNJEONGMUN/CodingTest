package LeetCode.DivideAndConquer.java;
/*
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/?envType=study-plan-v2&envId=top-interview-150
 */

public class convert_sorted_array_to_binary_search_tree {
    public static void main(String[] args) {
        Solution solution = new Solution();
        solution.sortedArrayToBST(new int[]{-10, -3, 0, 5, 9});
    }
}

class Solution {
    static TreeNode answer;

    public TreeNode sortedArrayToBST(int[] nums) {
        // M L R
        answer = solution(0, nums.length - 1, nums);
        System.out.println(answer);
        return answer;
    }

    public TreeNode solution(int left, int right, int[] nums) {
        if (left > right) {
            return null;
        }
        int mid = (left + right) / 2;
        return new TreeNode(
                nums[mid],
                solution(left, mid - 1, nums),
                solution(mid + 1, right, nums)
        );
    }
}


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    @Override
    public String toString() {
        return "val: " + val + "\n";
    }
}
