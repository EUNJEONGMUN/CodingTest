package Math.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class BOJ2480 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().trim().split(" ");
        int one = Integer.parseInt(input[0]);
        int two = Integer.parseInt(input[1]);
        int three = Integer.parseInt(input[2]);
        Set<Integer> set = new HashSet<>();
        set.add(one);
        set.add(two);
        set.add(three);

        if (set.size() == 1) {
            System.out.println(10000 + one * 1000);
        } else if (set.size() == 3) {
            System.out.println(Math.max(Math.max(one, two), three) * 100);
        } else {
            if (one == two) {
                System.out.println(1000 + one * 100);
            } else {
                System.out.println(1000 + three * 100);
            }
        }
    }
}
