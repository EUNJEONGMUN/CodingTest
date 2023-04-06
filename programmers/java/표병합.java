package programmers.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class 표병합 {

    public static void main(String[] args) {
        String[] commands = {"UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"};
        String[] commands2 = {"UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"};

        표병합_Solution solution = new 표병합_Solution();
        String[] res = solution.solution(commands);
        System.out.println(Arrays.toString(res));
        String[] res2 = solution.solution(commands2);
        System.out.println(Arrays.toString(res2));
    }
}


class 표병합_Solution {

    public static final int MAX_SIZE = 50;
    public static int[] index = new int[MAX_SIZE * MAX_SIZE];
    public static String[] table = new String[MAX_SIZE * MAX_SIZE];
    public static List<String> answer = new ArrayList<>();

    public String[] solution(String[] commands) {
        init();
        for (String command : commands) {
            String[] splitCommand = command.split(" ");
            switch (splitCommand[0]) {
                case "UPDATE":
                    if (splitCommand.length == 4) {
                        update(convertPosition(splitCommand[1], splitCommand[2]), splitCommand[3]);
                    } else {
                        replace(splitCommand[1], splitCommand[2]);
                    }
                    break;
                case "MERGE":
                    merge(convertPosition(splitCommand[1], splitCommand[2]),
                        convertPosition(splitCommand[3], splitCommand[4]));
                    break;
                case "UNMERGE":
                    unmerge(convertPosition(splitCommand[1], splitCommand[2]));
                    break;

                case "PRINT":
                    answer.add(print(convertPosition(splitCommand[1], splitCommand[2])));
                    break;

            }
        }

        String[] returnAnswer = new String[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            returnAnswer[i] = answer.get(i);
        }
        return returnAnswer;
    }

    private void init() {
        for (int i = 0; i < MAX_SIZE * MAX_SIZE; i++) {
            index[i] = i;
            table[i] = "EMPTY";
        }
    }


    private void update(int xy, String s) {
        for (int i = 0; i < MAX_SIZE * MAX_SIZE; i++) {
            if (index[i] == index[xy]) {
                table[i] = s;
            }
        }
    }

    private void replace(String s1, String s2) {
        for (int i = 0; i < MAX_SIZE * MAX_SIZE; i++) {
            if (table[i].equals(s1)) {
                table[i] = s2;
            }
        }
    }

    private void merge(int a, int b) {
        String val = "EMPTY";

        if (table[a] != "EMPTY") {
            val = table[a];
        } else if (table[b] != "EMPTY") {
            val = table[b];
        }

        int merge_idx = index[a];
        int old_idx = index[b];

        for (int i = 0; i < MAX_SIZE * MAX_SIZE; i++) {
            if (index[i] == old_idx) {
                index[i] = merge_idx;
                // 이 자리에서 table[i] = val이 안 되는 이유는, 원래 merge_idx인 곳도 있기 때문이다.
            }
        }
        if (!val.equals("EMPTY")){
            // EMPTY가 아닐 때만 VALUE를 갱신 -> 시간 감소
            for (int i = 0; i < MAX_SIZE * MAX_SIZE; i++) {
                if (index[i] == merge_idx) {
                    table[i] = val;
                }
            }
        }
    }

    private void unmerge(int xy) {
        String val = table[xy];
        int idx = index[xy];
        for (int i = 0; i < MAX_SIZE * MAX_SIZE; i++) {
            if (index[i] == idx) {
                index[i] = i;
                table[i] = "EMPTY";
            }
        }
        table[xy] = val;
    }

    private String print(int xy) {
        return table[xy];
    }

    private int convertPosition(String r, String c) {
        int x = Integer.parseInt(r);
        int y = Integer.parseInt(c);
        return (x - 1) * MAX_SIZE + (y - 1);
    }
}