package Greedy.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class BOJ2036 {

    static long answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> plus = new PriorityQueue<>(Comparator.reverseOrder());
        PriorityQueue<Integer> minus = new PriorityQueue<>();
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num > 0) {
                plus.offer(num);
            } else {
                minus.offer(num);
            }
        }
        answer += getAnswer(plus) + getAnswer(minus);

        System.out.println(answer);
    }

    public static long getAnswer(PriorityQueue<Integer> arr) {
        long res = 0;
        while (arr.size() > 1) {
            // arr에서 꺼낸 수를 long으로 형변환 해주지 않는다면,
            // 아래의 res += (a*b)와 같은 식에서 a*b를 먼저 계산하기 때문에 오버플로우 발생하는 것 같음...
            long a = arr.poll();
            long b = arr.poll();
            if (a == 1 || b == 1) {
                res += a + b;
            } else {
                res += a * b;
            }
        }
        if (arr.size() == 1) {
            res += arr.poll();
        }
        return res;
    }
}
