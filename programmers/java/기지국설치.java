package programmers.java;

public class 기지국설치 {

    public static void main(String[] args) {
        기지국설치_Solution solution = new 기지국설치_Solution();
        int[] stations = {4, 11};
        int ans = solution.solution(11, stations, 1);
        System.out.println(ans);

        int[] stations2 = {9};
        int ans2 = solution.solution(16, stations2, 2);
        System.out.println(ans2);

        int[] stations3 = {1, 6};
        int ans3 = solution.solution(16, stations3, 2);
        System.out.println(ans3);
    }
}

class 기지국설치_Solution {

    static int W, N;

    public int solution(int n, int[] stations, int w) {
        W = w;
        N = n;

        Answer answer = new Answer();

        for (int i = 0; i < stations.length; i++) {
            int left = Math.max(stations[i] - W, 1);
            int right = Math.min(stations[i] + W, N);

            if (i == 0) {
                answer.add(left - 1);
            } else {
                int beforeRight = Math.min(stations[i - 1] + W, N);
                answer.add(left - beforeRight - 1);
            }

            if (i == stations.length - 1) {
                answer.add(N - right);
            }
        }

        return answer.answer;
    }

    class Answer {
        int answer = 0;

        public void add(int value) {
            if (value>0) {
                int dist = W * 2 + 1;
                answer += value / dist;
                if (value % dist > 0) {
                    answer++;
                }
            }
        }
    }
}
