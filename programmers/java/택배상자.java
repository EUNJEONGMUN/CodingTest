package programmers.java;

import java.util.ArrayDeque;
import java.util.Deque;

public class 택배상자 {

}

class 택배상자_Solution {

    public int solution(int[] order) {
        Deque<Integer> q = new ArrayDeque<>();

        int nowBox = 1;
        int orderIdx = 0;
        int answer = 0;

        while (orderIdx < order.length) {
            if (nowBox == order[orderIdx]) {
                answer++;
                nowBox++;
                orderIdx++;
            } else if (nowBox < order[orderIdx]) {
                // 택배 기사님이 원하는 상자의 번호가 더 클 때
                q.offer(nowBox++);
            } else {
                // 택배 기사님이 원하는 상자의 번호가 더 작을 때
                if (!q.isEmpty() && q.peekLast() == order[orderIdx]) {
                    q.pollLast();
                    orderIdx++;
                    answer++;
                } else {
                    break;
                }
            }
        }
        return answer;
    }
}