package programmers.java;

import java.util.ArrayDeque;
import java.util.Deque;

public class 마법의엘리베이터 {

    public static void main(String[] args) {
        마법의엘리베이터_Solution solution = new 마법의엘리베이터_Solution();
        System.out.println(solution.solution(16)); // 6
        System.out.println(solution.solution(2554)); // 16
        System.out.println(solution.solution(678)); // 8
        System.out.println(solution.solution(999)); // 2
    }
}

class 마법의엘리베이터_Solution {

    public int solution(int storey) {
        Deque<Position> deque = new ArrayDeque<>();
        deque.push(new Position(storey, 0, 0));
        int max_digit = getDigit(storey)+1;
        int answer = Integer.MAX_VALUE;
        while (!deque.isEmpty()) {
            Position position = deque.poll();
            int now = position.storey;
            int count = position.count;
            int digit = position.digit;

            if (digit == max_digit) {
                // 종료 조건 : 현재 탐색하고 있는 자릿수가 max_digit과 같아졌을 때
                answer = Math.min(answer, count);
                continue;
            }

            int mod = now % 10;
            deque.push(new Position(now/10, count+mod, digit+1));
            deque.push(new Position(now/10+1, count+(10-mod), digit+1));
        }
        return answer;
    }

    public int getDigit(int num) {
        int d = 0;
        while (num>0){
            d++;
            num/=10;
        }
        return d;
    }
}

class Position {

    int storey;
    int count;
    int digit;

    public Position(int storey, int count, int digit) {
        this.storey = storey;
        this.count = count;
        this.digit = digit;
    }
}