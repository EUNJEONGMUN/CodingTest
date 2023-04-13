package programmers.java;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class 양과늑대 {

    public static void main(String[] args) {
        양과늑대_Solution solution = new 양과늑대_Solution();
        int[] info = {0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1};
        int[][] edges = {{0, 1}, {1, 2}, {1, 4}, {0, 8}, {8, 7}, {9, 10}, {9, 11}, {4, 3}, {6, 5},
            {4, 6}, {8, 9}};
        int ans = solution.solution(info, edges);
        System.out.println(ans);
    }

}

class 양과늑대_Solution {

    int answer = 0;
    boolean[] visited;
    Map<Integer, List<Node>> graph = new HashMap<>();

    public int solution(int[] info, int[][] edges) {
        visited = new boolean[info.length];
        for (int i = 0; i < edges.length; i++) {
            if (!graph.containsKey(edges[i][0])) {
                graph.put(edges[i][0], new ArrayList<>());
            }
            graph.get(edges[i][0]).add(new Node(info[edges[i][1]], edges[i][0], edges[i][1]));
        }
        visited[0] = true;
        dfs(1, 0);

        return answer;
    }

    private void dfs(int sheep, int wolf) {
        if (sheep > wolf) {
            answer = Math.max(answer, sheep);
        } else {
            return;
        }
        for (int i = 0; i < visited.length; i++) {
            if (visited[i] && graph.containsKey(i)) {
                List<Node> leaf = graph.get(i);
                for (Node node : leaf) {
                    if (!visited[node.nodeNum]) {
                        visited[node.nodeNum] = true;
                        if (node.status == 1) {
                            dfs(sheep, wolf + 1);
                        } else {
                            dfs(sheep + 1, wolf);
                        }
                        visited[node.nodeNum] = false;
                    }
                }
            }
        }
    }


    class Node {

        int status;
        int parent;
        int nodeNum;

        public Node(int status, int parent, int nodeNum) {
            this.status = status;
            this.parent = parent;
            this.nodeNum = nodeNum;
        }
    }
}