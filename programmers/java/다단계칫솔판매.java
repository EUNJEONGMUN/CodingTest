package programmers.java;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class 다단계칫솔판매 {

    public static void main(String[] args) {
        다단계칫솔판매_Solution solution = new 다단계칫솔판매_Solution();
        String[] enroll = {"john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"};
        String[] referral = {"-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"};
        String[] seller = {"young", "john", "tod", "emily", "mary"};
        int[] amount = {12, 4, 2, 5, 10};
        int[] answer = solution.solution(enroll, referral, seller, amount);
        System.out.println(Arrays.toString(answer));

        String[] seller2 = {"sam", "emily", "jaimie", "edward"};
        int[] amount2 = {2, 3, 5, 4};
        int[] answer2 = solution.solution(enroll, referral, seller2, amount2);
        System.out.println(Arrays.toString(answer2));
    }
}
class 다단계칫솔판매_Solution {
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        Map<String, Node> tree = new HashMap<>();
        for (int i=0; i<enroll.length; i++) {
            tree.put(enroll[i], new Node(enroll[i], referral[i]));
        }

        for (int i=0; i<seller.length; i++) {
            String now = seller[i];
            int move_profit = amount[i]*100;
            while (!now.equals("-")) {
                Node me = tree.get(now);
                if (move_profit<10) {
                    me.addProfit(move_profit);
                    break;
                }
                int temp = move_profit/10;
                me.addProfit(move_profit-temp);
                move_profit = temp;
                now = me.parent;
            }
        }
        List<Integer> answer = new ArrayList<>();
        for (String name : enroll) {
            answer.add(tree.get(name).profit);
        }
        return answer.stream().mapToInt(x -> x).toArray();

    }
    class Node{
        String name;
        String parent;
        int profit;

        public Node(String name, String parent) {
            this.name = name;
            this.parent = parent;
            this.profit = 0;
        }
        public void addProfit(int profit) {
            this.profit += profit;
        }
    }
}
