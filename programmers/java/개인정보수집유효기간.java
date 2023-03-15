package programmers.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class 개인정보수집유효기간 {

    public static void main(String[] args) {
        개인정보수집유효기간_Solution solution = new 개인정보수집유효기간_Solution();
        String today = "2022.05.19";
        String[] terms = {"A 6", "B 12", "C 3"};
        String[] privacies = {"2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"};
        int[] ans = solution.solution(today, terms, privacies);
        System.out.println(Arrays.toString(ans));
    }

}

class 개인정보수집유효기간_Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        MyDate today_convert = MyDate.createMyDate(today);
        System.out.println(today_convert.getDate());
        Map<String, Integer> term_map = new HashMap<>();
        Arrays.stream(terms).forEach(x -> {
            String[] s = x.split(" ");
            term_map.put(s[0], Integer.parseInt(s[1]));
        });

        List<Integer> answer = new ArrayList<>();
        for (int i=0; i<privacies.length; i++) {
            String[] privacy = privacies[i].split(" ");
            MyDate privacy_convert = MyDate.createMyDate(privacy[0], term_map.get(privacy[1]));
            if (today_convert.getDate() >= privacy_convert.getDate()) {
                answer.add(i+1);
            }
        }
        return answer.stream().mapToInt(x -> x).toArray();
    }
}

class MyDate {
    static int MONTH_DAY = 28;
    int date;

    private MyDate(int date) {
        this.date = date;
    }

    public static MyDate createMyDate(String str_date) {
        return new MyDate(convert_date(str_date));
    }

    public static MyDate createMyDate(String str_date, int month) {
        return new MyDate(convert_date(str_date) + month*MONTH_DAY);
    }

    private static int convert_date(String str_date) {
        String[] split = str_date.split("\\.");
        return (Integer.parseInt(split[0])*MONTH_DAY*12)
            + (Integer.parseInt(split[1])*MONTH_DAY)
            + Integer.parseInt(split[2]);
    }

    public int getDate() {
        return date;
    }
}