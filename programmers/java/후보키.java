package programmers.java;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;

public class 후보키 {

    public static void main(String[] args) {
        후보키_Solution solution = new 후보키_Solution();
        int ans = solution.solution(
            new String[][]{
                {"a","1","e","6"},
                {"a","2","e","7"},
                {"b","3","f","8"},
                {"c","4","g","9"},
                {"d","4","h","10"}
            });
        System.out.println(ans);


    }
}

class 후보키_Solution {

    List<Tuple<Integer>> logs = new ArrayList<>();
    int[] indexArr;
    List<Integer> now = new ArrayList<>();
    String[][] staticRelation;

    public int solution(String[][] relation) {
        indexArr = new int[relation[0].length];
        staticRelation = relation;
        int idx = 0;
        for (int i = 0; i < indexArr.length; i++) {
            indexArr[i] = idx++;
        }
        checkCombinations(0);
        return logs.size();
    }

    private void checkCombinations(int idx) {
        if (now.size() > 0 && isUnique()) { // 유일성을 만족시키는지 확인
            Tuple<Integer> nowTuple = new Tuple(now);
            boolean flag = true;
            for (int i = logs.size() - 1; i >= 0; i--) {
                if (logs.get(i).isDuplicateExists(nowTuple)) { // 겹치는 게 있는지 확인
                    if (logs.get(i).tuple.size() > nowTuple.tuple.size()) {
                        // logs에 있는 게 더 길이가 길 때, logs 안에 있는 게 최소성을 만족시키지 못하므로 지워야함.
                        logs.remove(logs.get(i));
                    } else {
                        // nowTuple이 더 길다면, nowTuple이 최소성을 만족시키지 못하므로 넣지 말아야 함.
                        flag = false;
                    }
                }
            }
            if (flag) {
                // nowTuple이 최소성을 만족시키거나,
                // logs 안에 겹치는 게 없을 때 logs에 add.
                logs.add(nowTuple);
            }
            return;
        }

        for (int i = idx; i < indexArr.length; i++) {
            now.add(i);
            checkCombinations(i + 1);
            now.remove(now.size() - 1);
        }

    }

    private boolean isUnique() {
        Set<Tuple<String>> checkSet = new HashSet<>();

        for (String[] strings : staticRelation) {
            List<String> stringList = new ArrayList<>();
            for (Integer i : now) {
                stringList.add(strings[i]);
            }
            Tuple<String> tuple = new Tuple<>(stringList);
            if (checkSet.contains(tuple)) {
                return false;
            }
            checkSet.add(tuple);
        }
        return true;
    }

    class Tuple<T> {

        final List<T> tuple = new ArrayList<>();

        Tuple(List<T> tuple) {
            this.tuple.addAll(tuple);
        }

        public boolean isDuplicateExists(Tuple other) {
            if (this.tuple.size() > other.tuple.size()) {
                return this.tuple.containsAll(other.tuple);
            }
            return other.tuple.containsAll(this.tuple);
        }

        @Override
        public int hashCode() {
            return Objects.hashCode(tuple);
        }

        @Override
        public boolean equals(Object obj) {
            if (!(obj instanceof Tuple)) {
                return false;
            }
            Tuple other = (Tuple) obj;
            if (other.tuple.size() != this.tuple.size()) {
                return false;
            }
            for (int i = 0; i < tuple.size(); i++) {
                if (!tuple.get(i).equals(other.tuple.get(i))) {
                    return false;
                }
            }
            return true;
        }
    }

}