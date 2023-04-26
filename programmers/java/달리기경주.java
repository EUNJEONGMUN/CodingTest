package programmers.java;

import java.util.HashMap;
import java.util.Map;

public class 달리기경주 {

}

class 달리기경주_Solution {

    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < players.length; i++) {
            map.put(players[i], i);
        }

        for (String calling : callings) {
            int callingIdx = map.get(calling);
            String beforeName = players[callingIdx - 1];

            players[callingIdx - 1] = calling;
            players[callingIdx] = beforeName;

            map.put(calling, callingIdx - 1);
            map.put(beforeName, callingIdx);
        }
        return players;
    }
}