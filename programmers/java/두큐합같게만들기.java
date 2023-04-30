package programmers.java;

import java.util.LinkedList;
import java.util.Queue;

public class 두큐합같게만들기 {

    public static void main(String[] args) {
        두큐합같게만들기_Solution solution = new 두큐합같게만들기_Solution();
        int ans = solution.solution(new int[]{3, 3, 3, 3}, new int[]{3, 3, 21, 3});
        System.out.println(ans);
    }
}

class 두큐합같게만들기_Solution {

    public int solution(int[] queue1, int[] queue2) {
        long q1Total = 0;
        long q2Total = 0;
        int answer = -1;

        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();

        for (int i = 0; i < queue1.length; i++) {
            q1Total += queue1[i];
            q1.offer(queue1[i]);

            q2Total += queue2[i];
            q2.offer(queue2[i]);
        }

        int count = 0;
        while (count <= queue1.length * 4) {
            if (q1Total == q2Total) {
                answer = count;
                break;
            }
            if (q1Total > q2Total) {
                int num = q1.poll();
                q2.offer(num);
                q1Total -= num;
                q2Total += num;
            } else {
                int num = q2.poll();
                q1.offer(num);
                q2Total -= num;
                q1Total += num;
            }
            count++;
        }
        return answer;
    }
}