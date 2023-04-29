package programmers.java;

import java.util.Comparator;
import java.util.PriorityQueue;

public class 디펜스게임 {

}

class 디펜스게임_Solution {

    public int solution(int n, int k, int[] enemy) {
        int idx = 0;
        PriorityQueue<Integer> queue = new PriorityQueue<>(Comparator.reverseOrder());
        while (idx < enemy.length) {
            if (n - enemy[idx] >= 0) {
                // 막을 수 있으면 막기
                queue.offer(enemy[idx]);
                n -= enemy[idx++];
            } else {
                if (k > 0) {
                    // 지금까지 가장 큰 적 vs 현재 적 비교
                    if (!queue.isEmpty() && queue.peek() >= enemy[idx]) {
                        // 가장 큰 적이 이전에 있을 때 -> 무적권 쓰기
                        int before = queue.poll();
                        n += before;
                    } else {
                        // 현재 적이 가장 클 때 -> 지금 무적권 쓰기
                        idx++;
                    }
                    k--;
                } else {
                    // 쓸 수 있는 무적권이 없다면 끝
                    break;
                }
            }
        }
        return idx;
    }
}