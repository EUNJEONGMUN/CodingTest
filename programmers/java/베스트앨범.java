package programmers.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

public class 베스트앨범 {

    public static void main(String[] args) {
        베스트앨범_Solution solution = new 베스트앨범_Solution();
        int[] ans = solution.solution(new String[]{"a","b","c","d","a","d","d","d","a","a","c","c"},
            new int[]{100,300,400,150,100,300,200,600,700,110,900,9000});
        System.out.println(Arrays.toString(ans));
    }
}

class 베스트앨범_Solution {

    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> map = new HashMap<>();
        List<Music> musicList = new ArrayList<>();
        List<Integer> answer = new ArrayList<>();

        for (int i = 0; i < genres.length; i++) {
            Music music = new Music(i, genres[i], plays[i]);
            map.put(genres[i], map.getOrDefault(genres[i], 0)+plays[i]);
            musicList.add(music);
        }

        Collections.sort(musicList);
        List<Map.Entry<String, Integer>> entryList = new LinkedList<>(map.entrySet());
        entryList.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));

        for (Entry<String, Integer> entry : entryList) {
            int count = 0;
            for (Music music : musicList) {
                if (music.genre.equals(entry.getKey())) {
                    answer.add(music.idx);
                    count++;
                }
                if (count>=2) {
                    break;
                }
            }
        }


        return answer.stream().mapToInt(o -> o).toArray();
    }

    class Music implements Comparable<Music> {

        int idx;
        String genre;
        int play;

        public Music(int idx, String genre, int play) {
            this.idx = idx;
            this.genre = genre;
            this.play = play;
        }

        @Override
        public int compareTo(Music o) {
            if (this.play == o.play) {
                return Integer.compare(this.idx, o.idx);
            }
            return Integer.compare(o.play, this.play);
        }
    }
}