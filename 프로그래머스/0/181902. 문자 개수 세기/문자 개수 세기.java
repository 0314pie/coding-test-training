import java.util.*;

class Solution {
    public int[] solution(String my_string) {
        Map<Character, Integer> abc = new HashMap<>();
        char upper = 'A';
        char lower = 'a';
        
        for (int i = 0; i <= 25; i++) {
            abc.put((char)(upper + i), 0);
            abc.put((char)(lower + i), 0);
        }
        
        for (char letter : my_string.toCharArray()) {
            if (abc.containsKey(letter)) {
                abc.put(letter, abc.get(letter) + 1);
            }
        }

        int[] answer = new int[52];
        int index = 0;
        for (int value : abc.values()) {
            answer[index++] = value;
        }

        return answer;
    }
}