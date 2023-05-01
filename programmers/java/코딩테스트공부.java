package programmers.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

public class 코딩테스트공부 {

    public static void main(String[] args) {
        코딩테스트공부_Solution2 solution = new 코딩테스트공부_Solution2();
        int a = solution.solution(10, 10,
            new int[][]{{10, 10, 2, 1, 2}, {10, 10, 3, 3, 4}});
        System.out.println(a);

        int ans = solution.solution(10, 10,
            new int[][]{{10, 15, 2, 1, 2}, {20, 20, 3, 3, 4}});
        System.out.println(ans);
        int ans2 = solution.solution(0, 0,
            new int[][]{{0, 0, 2, 1, 2}, {4, 5, 3, 1, 2}, {4, 11, 4, 0, 2}, {10, 4, 0, 4, 2}});
        System.out.println(ans2);
    }

}

class 코딩테스트공부_Solution {
    // 정확성 테스트만 통과

    int maxAlp;
    int maxCop;

    public int solution(int alp, int cop, int[][] problems) {
        List<Problem> problemList = new ArrayList<>();

        for (int[] problem : problems) {
            maxAlp = Math.max(maxAlp, problem[0]);
            maxCop = Math.max(maxCop, problem[1]);
            problemList.add(
                new Problem(problem[0], problem[1], problem[2], problem[3], problem[4]));
        }

        // {소요 시간, 알고력, 코딩력}
        PriorityQueue<int[]> queue = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });
        int answer = maxAlp + maxCop;
        queue.offer(new int[]{0, alp, cop});

        while (!queue.isEmpty()) {
            int[] now = queue.poll();

            if (canAllSolve(now[1], now[2])) {
                answer = now[0];
                break;
            }

            for (Problem problem : problemList) {
                if (problem.canSolve(now[1], now[2])) {
                    queue.offer(new int[]{
                        now[0] + problem.cost,
                        now[1] + problem.alp_rwd,
                        now[2] + problem.cop_rwd
                    });
                }
            }

            if (now[1] < maxAlp) {
                queue.offer(new int[]{
                    now[0] + 1,
                    now[1] + 1,
                    now[2]
                });
            }

            if (now[2] < maxCop) {
                queue.add(new int[]{
                    now[0] + 1,
                    now[1],
                    now[2] + 1
                });
            }
        }

        return answer;
    }

    private boolean canAllSolve(int alp, int cop) {
        if (alp >= maxAlp && cop >= maxCop) {
            return true;
        }
        return false;
    }

    class Problem {

        int alp_req;
        int cop_req;
        int alp_rwd;
        int cop_rwd;
        int cost;

        Problem(int alp_req, int cop_req, int alp_rwd, int cop_rwd, int cost) {
            this.alp_req = alp_req;
            this.cop_req = cop_req;
            this.alp_rwd = alp_rwd;
            this.cop_rwd = cop_rwd;
            this.cost = cost;
        }

        public boolean canSolve(int alp, int cop) {
            if (alp >= alp_req && cop >= cop_req) {
                return true;
            }
            return false;
        }
    }
}

class 코딩테스트공부_Solution2 {

    int maxAlp;
    int maxCop;

    public int solution(int alp, int cop, int[][] problems) {
        // dp[i][j] : (알고력 i, 코딩력 j) 상태에 도달하는 데 필요한 최단 시간

        for (int[] problem : problems) {
            maxAlp = Math.max(maxAlp, problem[0]);
            maxCop = Math.max(maxCop, problem[1]);
        }
        int[][] dp = new int[maxAlp + 1][maxCop + 1];

        for (int[] ints : dp) {
            Arrays.fill(ints, Integer.MAX_VALUE);
        }

        alp = Math.min(alp, maxAlp);
        cop = Math.min(cop, maxCop);

        dp[alp][cop] = 0;

        for (int i = alp; i <= maxAlp; i++) {
            for (int j = cop; j <= maxCop; j++) {
                if (i < maxAlp) {
                    dp[i + 1][j] = Math.min(dp[i][j] + 1, dp[i + 1][j]);
                }
                if (j < maxCop) {
                    dp[i][j + 1] = Math.min(dp[i][j] + 1, dp[i][j + 1]);
                }

                for (int[] problem : problems) {
                    if (problem[0] <= i && problem[1] <= j) {
                        int nextAlp = Math.min(i + problem[2], maxAlp);
                        int nextCop = Math.min(j + problem[3], maxCop);
                        dp[nextAlp][nextCop] = Math.min(dp[i][j] + problem[4],
                            dp[nextAlp][nextCop]);
                    }
                }

            }
        }
        return dp[maxAlp][maxCop];
    }
}