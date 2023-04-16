package programmers.java;

public class 나머지가1이되는수찾기 {

}
class 나머지가1이되는수찾기_Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i=2; i<n; i++) {
            if ((n-1)%i==0) {
                answer = i;
                break;
            }
        }
        return answer;
    }
}