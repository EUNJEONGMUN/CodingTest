package String.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class BOJ5052 {
    static int TC;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        TC = Integer.parseInt(br.readLine());

        while (TC-- > 0) {
            int N = Integer.parseInt(br.readLine());
            List<String> list = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                list.add(br.readLine().trim());
            }
            list.sort(String::compareTo); // 정렬
            if (solution(list)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }

    private static boolean solution(List<String> list) {
        // 리스트가 이미 정렬 된 상태이기 때문에, 두 개씩만 비교하면 됨.
        // string 정렬이어서 길이 정렬도 된 상태.
        // 앞의 번호가 뒤의 번호에 완전히 포함될 떄 접두어이다.
        for (int i = 0; i < list.size() - 1; i++) {
            String A = list.get(i);
            String B = list.get(i + 1);

            if (A.length() <= B.length()) {
                if (B.substring(0, A.length()).equals(A)) {
                    return false;
                }
            }
        }
        return true;
    }
}
