package LeetCode.BitManipulation.java;
/*
https://leetcode.com/problems/add-binary/?envType=study-plan-v2&envId=top-interview-150
 */

import java.math.BigInteger;

public class add_binary {
    public static void main(String[] args) {
        String a = "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101";
        String b = "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011";
        Solution solution = new Solution();
        System.out.println(solution.addBinary(a, b));
    }
}

class Solution {
    public String addBinary(String a, String b) {
//        return Integer.toBinaryString(Integer.parseInt(a,2)+Integer.parseInt(b,2));
        BigInteger bigIntegerA = new BigInteger(a, 2);
        BigInteger bigIntegerB = new BigInteger(b, 2);
        return bigIntegerA.add(bigIntegerB).toString(2);
    }
}
