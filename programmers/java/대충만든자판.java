package programmers.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class 대충만든자판 {

    public static void main(String[] args) {
        String[] key_map = {"AGZ", "BSSS"};
        String[] targets = {"ASA","BGZ"};

        대충만든자판_Solution solution = new 대충만든자판_Solution();
        int[] ans = solution.solution(key_map, targets);
        System.out.println(Arrays.toString(ans));
    }
}

class 대충만든자판_Solution {

    public int[] solution(String[] keymaps, String[] targets) {
        Map<Character, Integer> record = new HashMap<>();

        for (String keymap : keymaps) {
            for (int i = 0; i < keymap.length(); i++) {
                if (record.containsKey(keymap.charAt(i))) {
                    if (record.get(keymap.charAt(i)) > i + 1) {
                        record.put(keymap.charAt(i), i + 1);
                    }
                } else {
                    record.put(keymap.charAt(i), i + 1);
                }
            }
        }

        List<Integer> answer = new ArrayList<>();
        for (String target : targets) {
            int ans = 0;
            for (int i=0; i<target.length(); i++) {
                if (record.containsKey(target.charAt(i))) {
                    ans += record.get(target.charAt(i));
                } else {
                    ans = -1;
                    break;
                }
            }
            answer.add(ans);
        }
        return answer.stream().mapToInt(x -> x).toArray();
    }
}

