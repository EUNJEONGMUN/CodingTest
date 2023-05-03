package programmers.java;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class 단체사진찍기 {

    public static void main(String[] args) {
        단체사진찍기_Solution solution = new 단체사진찍기_Solution();
        int ans = solution.solution(2, new String[]{"N~F=0", "R~T>2"});
        System.out.println(ans);
    }
}


class 단체사진찍기_Solution {

    int answer = 0;
    char[] names = new char[]{'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};
    List<Integer> indexes = new ArrayList<>();
    String[] staticData;

    public int solution(int n, String[] data) {

        staticData = data;
        combi(0);
        return answer;
    }

    private void combi(int depth) {
        if (indexes.size() == 8) {
            if (check()) {
                answer++;
            }
            return;

        }

        for (int i = 0; i < 8; i++) {
            if (!indexes.contains(i)) {
                indexes.add(i);
                combi(depth + 1);
                indexes.remove(indexes.size() - 1);
            }
        }
    }

    private boolean check() {
        HashMap<Character, Integer> orders = new HashMap<>();
        for (int i = 0; i < 8; i++) {
            orders.put(names[indexes.get(i)], i);
        }

        for (String d : staticData) {
            int diff = d.charAt(4) - '0';

            if (d.charAt(3) == '=') {
                if (Math.abs(orders.get(d.charAt(0)) - orders.get(d.charAt(2))) - 1 != diff) {
                    return false;
                }
            } else if (d.charAt(3) == '>') {
                if (Math.abs(orders.get(d.charAt(0)) - orders.get(d.charAt(2))) - 1 <= diff) {
                    return false;
                }
            } else if (d.charAt(3) == '<') {
                if (Math.abs(orders.get(d.charAt(0)) - orders.get(d.charAt(2))) - 1 >= diff) {
                    return false;
                }
            }
        }
        return true;
    }
}