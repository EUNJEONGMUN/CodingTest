package programmers.java;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;

public class 호텔대실 {

}

class 호텔대실_Solution {

    public int solution(String[][] bookTime) {
        List<Book> bookList = new ArrayList<>();

        for (String[] time : bookTime) {
            bookList.add(new Book(time[0], time[1]));
        }

        Collections.sort(bookList, ((o1, o2) -> {
            return Integer.compare(o1.startTime, o2.startTime);
        }));

        PriorityQueue<Book> queue = new PriorityQueue<>(((o1, o2) -> {
            return Integer.compare(o1.endTime, o2.endTime);
        }));

        int answer = 1;
        for (Book book : bookList) {
            if (queue.isEmpty() || queue.peek().endTime + 10 <= book.startTime) {
                queue.poll();
            } else {
                answer++;
            }
            queue.offer(book);
        }
        return answer;
    }

    class Book {

        int startTime;
        int endTime;

        public Book(String s, String e) {
            String[] startSplit = s.split(":");
            String[] endSplit = e.split(":");
            this.startTime = Integer.parseInt(startSplit[0]) * 60 + Integer.parseInt(startSplit[1]);
            this.endTime = Integer.parseInt(endSplit[0]) * 60 + Integer.parseInt(endSplit[1]);
        }
    }
}