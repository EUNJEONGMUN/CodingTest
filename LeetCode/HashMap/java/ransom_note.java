package LeetCode.HashMap.java;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/*
https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
 */
public class ransom_note {
    public static void main(String[] args) {
        canConstructBestSolution("aa", "ab");
    }
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> ransomNoteMap = makeHashMap(ransomNote);
        Map<Character, Integer> magazineMap = makeHashMap(magazine);

        for (Character key : ransomNoteMap.keySet()) {
            if (!magazineMap.containsKey(key)) {
                return false;
            }
            if (ransomNoteMap.get(key) > magazineMap.get(key)) {
                return false;
            }
        }
        return true;
    }

    private Map<Character, Integer> makeHashMap(String str) {
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < str.length(); i++) {
            if (!map.containsKey(str.charAt(i))) {
                map.put(str.charAt(i), 0);
            }
            map.put(str.charAt(i), map.get(str.charAt(i)) + 1);
        }
        return map;
    }

    public static boolean canConstructBestSolution(String ransomNote, String magazine) {
        int[] alphabet = new int[26];

        for (int i = 0; i < magazine.length(); i++) {
            alphabet[magazine.charAt(i) - 'a']++;
            System.out.println(magazine.charAt(i) - 'a');
        }
        System.out.println(Arrays.toString(alphabet));
        for (int i = 0; i < ransomNote.length(); i++) {
            int idx = ransomNote.charAt(i) - 'a';
            if (alphabet[idx] == 0) {
                return false;
            }
            alphabet[idx]--;
        }
        return true;
    }
}
