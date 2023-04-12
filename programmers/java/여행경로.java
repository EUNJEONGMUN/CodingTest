package programmers.java;

import java.util.Arrays;

public class 여행경로 {

    public static void main(String[] args) {
        여행경로_Solution solution = new 여행경로_Solution();
        String[][] tickets = {{"ICN", "SFO"}, {"ICN", "ATL"}, {"SFO", "ATL"}, {"ATL", "ICN"},
            {"ATL", "SFO"}};
        String[] ans = solution.solution(tickets);
        System.out.println(Arrays.toString(ans));
    }
}

class 여행경로_Solution {

    int N;
    boolean[] visited;
    String[] log;
    String[] answer;

    public String[] solution(String[][] tickets) {
        N = tickets.length;
        visited = new boolean[N];
        log = new String[N + 1];

        Arrays.sort(tickets, (o1, o2) -> {
            if (o1[0].equals(o2[0])) {
                return o1[1].compareTo(o2[1]);
            }
            return o1[0].compareTo(o2[0]);
        });

        log[0] = "ICN";
        dfs(1, tickets);

        return answer;
    }

    private void dfs(int depth, String[][] tickets) {
        if (depth == N + 1) {
            if (answer == null) {
                answer = log.clone();
            }
            return;
        }

        for (int i = 0; i < N; i++) {
            if (tickets[i][0].equals(log[depth - 1]) && !visited[i]) {
                visited[i] = true;
                log[depth] = tickets[i][1];
                dfs(depth + 1, tickets);
                visited[i] = false;
            }
        }
    }
}