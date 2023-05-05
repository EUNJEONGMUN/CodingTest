package programmers.java;

public class 두원사이의정수쌍 {

    public static void main(String[] args) {
        두원사이의정수쌍_Solution solution = new 두원사이의정수쌍_Solution();
        long ans = solution.solution(4, 5);
        System.out.println(ans);
    }
}

class 두원사이의정수쌍_Solution {

    public long solution(int r1, int r2) {
        long answer = 0;
        long R1 = r1;
        long R2 = r2;

        for (long i = 1; i <= R2; i++) {
            long r2y = (long) Math.floor(Math.sqrt(R2 * R2 - i * i));
            long r1y;
            if (i > r1) {
                r1y = 0;
            } else {
                r1y = (long) Math.ceil(Math.sqrt(R1 * R1 - i * i));
            }
            answer += (r2y - r1y + 1);
        }
        return (answer) * 4;
    }
}