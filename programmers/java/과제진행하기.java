package programmers.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

public class 과제진행하기 {

    public static void main(String[] args) {
        과제진행하기_Solution solution = new 과제진행하기_Solution();
        String[] ans = solution.solution(
            new String[][]{{"korean", "11:40", "30"}, {"english", "12:10", "20"},
                {"math", "12:30", "40"}});
        System.out.println(Arrays.toString(ans));
        String[] ans2 = solution.solution(
            new String[][]{{"science", "12:40", "50"}, {"music", "12:20", "40"},
                {"history", "14:00", "30"}, {"computer", "12:30", "100"}});
        System.out.println(Arrays.toString(ans2));

        String[] ans3 = solution.solution(
            new String[][]{{"1", "00:00", "30"}, {"2", "00:10", "10"}, {"3", "00:30", "10"},
                {"4", "00:50", "10"}});
        System.out.println(Arrays.toString(ans3));
    }
}

class 과제진행하기_Solution {

    public String[] solution(String[][] plans) {
        List<String> answer = new ArrayList<>();
        List<Work> works = new ArrayList<>();
        for (String[] plan : plans) {
            works.add(new Work(plan[0], plan[1], plan[2]));
        }
        Collections.sort(works);

        Stack<Work> stack = new Stack<>();
        int workIdx = 0;

        int nowTime = works.get(workIdx).startTime;
        Work nowWork = works.get(workIdx++);
        Work nextWork = works.get(workIdx++);

        while (nextWork != null) {
            if (nowWork.calculateFinishTime(nowTime) <= nextWork.startTime) {
                // 다음 일 시작 전에 끝낼 수 있을 때
                answer.add(nowWork.name);
                if (!stack.isEmpty()) {
                    nowTime = nowWork.calculateFinishTime(nowTime);
                    nowWork = stack.pop();
                    continue;
                }
            } else {
                // 다음 일 시작 전에 끝낼 수 없을 때
                nowWork.reduceRemainTime(nowTime, nextWork.startTime);
                stack.push(nowWork);
            }
            nowTime = nextWork.startTime;
            nowWork = nextWork;
            if (workIdx < works.size()) {
                nextWork = works.get(workIdx++);
            } else {
                // 마지막 작업일 때
                answer.add(nowWork.name);
                nextWork = null;
            }
        }

        // 나머지 작업들 해주기
        while (!stack.isEmpty()) {
            answer.add(stack.pop().name);
        }

        return answer.toArray(new String[answer.size()]);
    }


    class Work implements Comparable<Work> {

        String name;
        int startTime;
        int remainTime;

        public Work(String name, String t, String w) {
            this.name = name;
            String[] split = t.split(":");
            this.startTime = Integer.parseInt(split[0]) * 60 + Integer.parseInt(split[1]);
            this.remainTime = Integer.parseInt(w);
        }

        public int calculateFinishTime(int now) {
            return now + remainTime;
        }

        public void reduceRemainTime(int now, int nextTime) {
            this.remainTime -= (nextTime - now);
        }

        @Override
        public int compareTo(Work o) {
            return this.startTime - o.startTime;
        }
    }
}