package programmers.java;

import java.util.ArrayDeque;
import java.util.Deque;

public class 마법의엘리베이터 {

    public static void main(String[] args) {
        마법의엘리베이터2_Solution solution = new 마법의엘리베이터2_Solution();
        System.out.println(solution.solution(16)); // 6
        System.out.println(solution.solution(2554)); // 16
        System.out.println(solution.solution(678)); // 8
        System.out.println(solution.solution(999)); // 2
        System.out.println(solution.solution(535));
        System.out.println(solution.solution(575));
        System.out.println(solution.solution(545));
        System.out.println(solution.solution(555));

        마법의엘리베이터3_Solution solution2 = new 마법의엘리베이터3_Solution();
        System.out.println(solution2.solution(16)); // 6
        System.out.println(solution2.solution(2554)); // 16
        System.out.println(solution2.solution(678)); // 8
        System.out.println(solution2.solution(999)); // 2
        System.out.println(solution2.solution(535));
        System.out.println(solution2.solution(575));
        System.out.println(solution2.solution(545));
        System.out.println(solution2.solution(555));
    }
}

class 마법의엘리베이터_Solution {

    public int solution(int storey) {
        Deque<Position> deque = new ArrayDeque<>();
        deque.push(new Position(storey, 0, 0));
        int max_digit = getDigit(storey) + 1;
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
            deque.push(new Position(now / 10, count + mod, digit + 1));
            deque.push(new Position(now / 10 + 1, count + (10 - mod), digit + 1));
        }
        return answer;
    }

    public int getDigit(int num) {
        int d = 0;
        while (num > 0) {
            d++;
            num /= 10;
        }
        return d;
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

}


class 마법의엘리베이터2_Solution {

    public int solution(int storey) {
        Deque<Position> deque = new ArrayDeque<>();
        deque.push(new Position(storey, 0));
        int answer = Integer.MAX_VALUE;
        while (!deque.isEmpty()) {
            Position position = deque.poll();
            int now = position.storey;
            int count = position.count;

            if (now == 10) {
                answer = Math.min(answer, count + 1);
                continue;
            }

            if (now <= 5) {
                answer = Math.min(answer, count + now);
                continue;
            }

            int mod = now % 10;
            deque.push(new Position(now / 10, count + mod));
            deque.push(new Position(now / 10 + 1, count + (10 - mod)));
        }
        return answer;
    }
    class Position {
        int storey;
        int count;
        public Position(int storey, int count) {
            this.storey = storey;
            this.count = count;
        }
    }
}

class 마법의엘리베이터3_Solution {

    public int solution(int storey) {
        Deque<Position> deque = new ArrayDeque<>();
        deque.push(new Position(storey, 0));
        int answer = Integer.MAX_VALUE;
        while (!deque.isEmpty()) {
            Position position = deque.poll();
            int now = position.storey;
            int count = position.count;

            if (now == 10) {
                answer = Math.min(answer, count + 1);
                continue;
            }

            if (now == 0) {
                answer = Math.min(answer, count);
                continue;
            }

            int mod = now % 10;
            now /= 10;
            if (mod > 5 || (mod == 5 && now % 10 >= 5)) {
                // mod가 5보다 클 때
                // mod가 5와 같을 때는 앞에가 5와 같거나 클 때
                // 5와 같을 때도 포함시키는 이유는, 앞의 수가 5보다 크면, 자릿수가 올라가서 더욱 10에 가까워질 수 있기 때문이다.
                deque.push(new Position(now + 1, count + (10 - mod)));
            } else {
                deque.push(new Position(now, count + mod));
            }
        }
        return answer;
    }
    class Position {
        int storey;
        int count;
        public Position(int storey, int count) {
            this.storey = storey;
            this.count = count;
        }
    }
}