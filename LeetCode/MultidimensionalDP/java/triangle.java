package LeetCode.MultidimensionalDP.java;
/*
https://leetcode.com/problems/triangle/?envType=study-plan-v2&envId=top-interview-150
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class triangle {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> one = new ArrayList<>(List.of(2));
        List<Integer> two = new ArrayList<>(List.of(3, 4));
        List<Integer> three = new ArrayList<>(List.of(6, 5, 7));
        List<Integer> four = new ArrayList<>(List.of(4, 1, 8, 3));
        List<List<Integer>> arr = new ArrayList<>();
        arr.add(one);
        arr.add(two);
        arr.add(three);
        arr.add(four);
        System.out.println(solution.minimumTotal(arr));
    }
}

class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        for (int i = 1; i < triangle.size(); i++) {
            List<Integer> nowRow = triangle.get(i);
            for (int j = 0; j < nowRow.size(); j++) {
                int num = nowRow.get(j);
                if (j == 0) {
                    nowRow.set(j, num + triangle.get(i - 1).get(j));
                } else if (j == nowRow.size() - 1) {
                    nowRow.set(j, num + triangle.get(i - 1).get(j - 1));
                } else {
                    nowRow.set(j, num + Math.min(triangle.get(i - 1).get(j - 1), triangle.get(i - 1).get(j)));
                }
            }
        }
        return Collections.min(triangle.get(triangle.size() - 1));
    }
}