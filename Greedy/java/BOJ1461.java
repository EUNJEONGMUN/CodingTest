package Greedy.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ1461 {
    static List<Integer> plus = new LinkedList<>();
    static List<Integer> minus = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());
            if (num > 0) {
                plus.add(num);
            } else {
                minus.add(num);
            }
        }

        int answer = 0;

        Collections.sort(plus, Collections.reverseOrder());
        Collections.sort(minus);

        for (int i = 0; i < plus.size(); i += M) {
            answer += plus.get(i) * 2;
        }


        for (int i = 0; i < minus.size(); i += M) {
            answer += Math.abs(minus.get(i)) * 2;
        }


        if (plus.size() == 0 || minus.size() > 0 && (plus.get(0) < Math.abs(minus.get(0)))) {
            answer -= Math.abs(minus.get(0));
        } else {
            answer -= plus.get(0);
        }

        System.out.println(answer);
    }
}
