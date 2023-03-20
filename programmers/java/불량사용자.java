package programmers.java;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.stream.Collectors;

public class 불량사용자 {

    public static void main(String[] args) {
        불량사용자_Solution solution = new 불량사용자_Solution();
        String[] user_id = {"frodo", "fradi", "crodo", "abc123", "frodoc"};
        String[] banned_id = {"fr*d*", "abc1**"};
        int ans = solution.solution(user_id, banned_id);
        System.out.println(ans);

        String[] user_id2 = {"frodo", "fradi", "crodo", "abc123", "frodoc"};
        String[] banned_id2 = {"*rodo", "*rodo", "******"};
        int ans2 = solution.solution(user_id2, banned_id2);
        System.out.println(ans2);

        String[] user_id3 = {"frodo", "fradi", "crodo", "abc123", "frodoc"};
        String[] banned_id3 = {"fr*d*", "*rodo", "******", "******"};
        int ans3 = solution.solution(user_id3, banned_id3);
        System.out.println(ans3);
    }
}

class 불량사용자_Solution {

    List<List<String>> banList = new ArrayList<>();
    HashSet<List<String>> answerList = new HashSet<>();

    public int solution(String[] user_id, String[] banned_id) {
        for (int b = 0; b < banned_id.length; b++) {
            List<String> list = new ArrayList<>();
            for (int u = 0; u < user_id.length; u++) {
                if (isSame(banned_id[b], user_id[u])) {
                    list.add(user_id[u]);
                }
            }
            banList.add(list);
        }

        dfs(new HashSet<>());
        return answerList.size();
    }

    private void dfs(HashSet<String> ban) {
        if (ban.size() == banList.size()) {
            answerList.add(ban.stream().sorted().collect(Collectors.toList()));
            return;
        }
        for (int j = 0; j < banList.get(ban.size()).size(); j++) {
            int i = ban.size();
            if (!ban.contains(banList.get(i).get(j))) {
                ban.add(banList.get(i).get(j));
                dfs(ban);
                ban.remove(banList.get(i).get(j));
            }
        }
    }

    private boolean isSame(String ban, String name) {
        if (ban.length() != name.length()) {
            return false;
        }
        for (int i = 0; i < name.length(); i++) {
            if (ban.charAt(i) != '*' && name.charAt(i) != ban.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}