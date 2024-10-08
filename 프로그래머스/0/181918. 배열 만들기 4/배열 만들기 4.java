import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        Deque<Integer> deque = new ArrayDeque<>();
        
        int i = 0;
        while (i < arr.length) {
            if (deque.isEmpty()) {
                deque.addLast(arr[i]);
                i++;
            } else if (deque.peekLast() < arr[i]) {
                deque.addLast(arr[i]);
                i++;
            } else {
                deque.removeLast();
            }
        }

        int[] result = new int[deque.size()];
        int index = 0;
        for (int num : deque) {
            result[index++] = num;
        }
        
        return result;
    }
}