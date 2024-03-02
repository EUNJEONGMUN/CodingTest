package LeetCode.GraphBFS.java;
/*
https://leetcode.com/problems/minimum-genetic-mutation/?envType=study-plan-v2&envId=top-interview-150
 */
import java.util.LinkedList;
import java.util.Queue;

public class minimum_genetic_mutation {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.minMutation("AACCGGTT", "AAACGGTA", new String[]{"AACCGGTA", "AACCGCTA", "AAACGGTA"}));
    }
}

class Solution {
    public int minMutation(String startGene, String endGene, String[] bank) {
        boolean[] visited = new boolean[bank.length];
        Queue<Tuple> queue = new LinkedList<>();

        for (int i = 0; i < bank.length; i++) {
            if (isOneDifferent(bank[i], startGene)) {
                queue.offer(new Tuple(bank[i], 1));
                visited[i] = true;
            }
        }

        while (!(queue.isEmpty())) {
            Tuple now = queue.poll();
            if (endGene.equals(now.s)) {
                return now.count;
            }

            for (int i = 0; i < bank.length; i++) {
                if (!visited[i] && isOneDifferent(bank[i], now.s)) {
                    queue.offer(new Tuple(bank[i], now.count + 1));
                    visited[i] = true;
                }
            }
        }
        return -1;


    }


    private boolean isOneDifferent(String A, String B) {
        int diffCount = 0;
        for (int i = 0; i < A.length(); i++) {
            if (A.charAt(i) != B.charAt(i)) {
                diffCount++;
            }
        }
        return diffCount == 1;
    }

    class Tuple {
        String s;
        int count;

        public Tuple(String s, int count) {
            this.s = s;
            this.count = count;
        }
    }
}