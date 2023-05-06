package programmers.java;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class 혼자놀기의달인 {

}


class 혼자놀기의달인_Solution {

    public int solution(int[] cards) {
        boolean[] check = new boolean[cards.length];
        List<Integer> counts = new ArrayList<>();
        for (int i = 0; i < cards.length; i++) {
            if (check[i] == true) {
                continue;
            }
            int idx = i;
            int cnt = 0;
            while (!check[idx]) {
                check[idx] = true;
                idx = cards[idx] - 1;
                cnt++;
            }
            if (cnt > 0) {
                counts.add(cnt);
            }
        }
        if (counts.size() < 2) {
            return 0;
        }
        Collections.sort(counts, Comparator.reverseOrder());
        return counts.get(0) * counts.get(1);
    }
}