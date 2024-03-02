package LeetCode.Backtracking.java;
/*
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=top-interview-150
 */
import java.util.ArrayList;
import java.util.List;

public class letter_combinations_of_a_phone_number {
    static List<String> answer = new ArrayList<>();
    static String[] letters = new String[]{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public static void main(String[] args) {
        letterCombinations("");
    }

    public static List<String> letterCombinations(String digits) {
        String[] split = digits.split("");
        if (!digits.equals("")) {
            solution(split, 0, "");
        }
        return answer;
    }

    public static void solution(String[] digits, int depth, String word) {
        if (digits.length == depth) {
            answer.add(word);
            return;
        }

        String nowLetters = letters[Integer.parseInt(digits[depth])];

        for (int i = 0; i < nowLetters.length(); i++) {
            solution(digits, depth+1, word+nowLetters.charAt(i));
        }
    }
}