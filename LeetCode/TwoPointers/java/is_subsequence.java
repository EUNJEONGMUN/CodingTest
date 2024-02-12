package LeetCode.TwoPointers.java;

/*
https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150
 */
public class is_subsequence {
    public static void main(String[] args) {
        System.out.println(isSubsequence("abc", "ahbgdc")); // true
        System.out.println(isSubsequence("axc", "ahbgdc")); // false
        System.out.println(isSubsequence("", "ahbgdc")); // true
    }

    public static boolean isSubsequence(String s, String t) {
        // subsequence -> 부분 수열
        // s가 t의 subsequence이면 true, 아니면 false

        int sLen = s.length();
        int tLen = t.length();

        if (sLen > tLen) {
            // t의 길이가 짧을 경우 부분수열이 될 수 없음.
            return false;
        }

        int idx = 0;
        for (int i = 0; i < tLen; i++) {
            if (idx == sLen) {
                break;
            }
            if (s.charAt(idx) == t.charAt(i)) {
                idx++;
            }
        }

        if (idx == sLen) {
            return true;
        }
        return false;
    }
}
