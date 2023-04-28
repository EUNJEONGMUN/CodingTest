package programmers.java;

import java.util.HashMap;
import java.util.Map;

public class 할인행사 {

}

class 할인행사_Solution {

    public int solution(String[] wants, int[] number, String[] discount) {
        int answer = 0;
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < number.length; i++) {
            map.put(wants[i], number[i]);
        }
        for (int i = 0; i < 10; i++) {
            if (map.containsKey(discount[i])) {
                map.put(discount[i], map.get(discount[i]) - 1);
            }
        }

        int left = 0;
        int right = 9;

        while (true) {
            if (isAllDiscount(map)) {
                answer++;
            }

            if (right + 1 >= discount.length) {
                break;
            }
            right++;
            if (map.containsKey(discount[right])) {
                map.put(discount[right], map.get(discount[right]) - 1);
            }
            if (map.containsKey(discount[left])) {
                map.put(discount[left], map.get(discount[left]) + 1);
            }
            left++;

        }

        return answer;
    }

    private boolean isAllDiscount(Map<String, Integer> map) {
        for (Integer cnt : map.values()) {
            if (cnt > 0) {
                return false;
            }
        }
        return true;

    }
}