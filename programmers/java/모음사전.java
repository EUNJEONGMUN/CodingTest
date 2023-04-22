package programmers.java;

public class 모음사전 {

    public static void main(String[] args) {
        모음사전_Solution solution = new 모음사전_Solution();
        int ans = solution.solution("AAAE");
        System.out.println(ans);
    }
}
class 모음사전_Solution {
    int answer = 0;
    String[] alphabet = {"A", "E", "I", "O", "U"};
    public int solution(String word) {
        dfs("", word);
        return answer-1;
    }

    private boolean dfs(String str, String word) {
        answer++;
        if (str.equals(word)) {
            return true;
        }
        if (str.length() == 5) {
            return false;
        }

        for (int i=0; i<5; i++) {
            if (dfs(str.concat(alphabet[i]), word)) {
                return true;
            }
        }
        return false;
    }
}