package String.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BOJ20437 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < T; tc++) {
            String W = br.readLine();
            int K = Integer.parseInt(br.readLine());

            Map<String, List<Integer>> map = new HashMap<>();
            String[] split = W.split("");

            for (int idx = 0; idx < split.length; idx++) {
                if (!map.containsKey(split[idx])) {
                    map.put(split[idx], new ArrayList<>());
                }
                map.get(split[idx]).add(idx);
            }

            int shortest = Integer.MAX_VALUE;
            int longest = -1;

            for (List<Integer> indexes : map.values()) {
                if (indexes.size() >= K) {
                    int left = 0;
                    for (int right = K - 1; right < indexes.size(); right++) {
                        shortest = Math.min(shortest, indexes.get(right) - indexes.get(left) + 1);
                        longest = Math.max(longest, indexes.get(right) - indexes.get(left) + 1);
                        left++;
                    }
                }
            }

            if (shortest == Integer.MAX_VALUE) {
                System.out.println(-1);
            } else {
                System.out.println(shortest + " " + longest);
            }
        }
    }
}
