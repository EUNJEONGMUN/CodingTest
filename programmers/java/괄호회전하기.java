package programmers.java;

import java.util.Stack;

class 괄호회전하기_Solution {

    static Stack<Character> stack;
    static char[] arr;


    public int solution(String s) {
        int answer = 0;
        arr = s.toCharArray();
        for (int split = 0; split < s.length(); split++) {
            stack = new Stack<>();
            boolean ans = getAnswer(split, s.length());
            if (ans) {
                ans = getAnswer(0, split);
            }
            if (ans && stack.empty()) {
                answer++;
            }
        }
        return answer;
    }

    private boolean getAnswer(int start, int end) {
        for (int i = start; i < end; i++) {
            if (arr[i] == '(' || arr[i] == '{' || arr[i] == '[') {
                stack.push(arr[i]);
            } else {
                if (stack.size() == 0) {
                    return false;
                }
                if ((arr[i] == ')' && stack.peek() == '(') ||
                    (arr[i] == '}' && stack.peek() == '{') ||
                    (arr[i] == ']' && stack.peek() == '[')) {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        return true;
    }
}