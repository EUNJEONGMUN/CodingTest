package Tree.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ3584 {
    static int TC;
    static BufferedReader br;
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        TC = Integer.parseInt(br.readLine());

        for (int i=0; i<TC; i++) {
            int N = Integer.parseInt(br.readLine());
            solution(N);
        }
    }

    private static void solution(int N) throws IOException {
        int[] parents = new int[N+1];

        for (int j=0; j<N-1; j++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            parents[b] = a;
        }
        st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        List<Integer> aParents = new ArrayList<>(List.of(a)); // a의 부모들 저장
        List<Integer> bParents = new ArrayList<>(List.of(b)); // b의 부모들 저장

        aParents.addAll(dfs(parents, a, new ArrayList<>()));
        bParents.addAll(dfs(parents, b, new ArrayList<>()));

        for (Integer aParent : aParents) { // a의 부모들을 아래서 위로 올라가면서 b에 포함된 게 있는지 확인. 루트 노드에서는 무조건 만나기 때문에 답은 도출됨.
            if (bParents.contains(aParent)) {
                System.out.println(aParent);
                break;
            }
        }
    }

    private static List<Integer> dfs(int[] parents, int idx, List<Integer> res) {
        if (parents[idx] == 0) {
            return res;
        }
        res.add(parents[idx]);
        dfs(parents, parents[idx], res);
        return res;
    }
}
