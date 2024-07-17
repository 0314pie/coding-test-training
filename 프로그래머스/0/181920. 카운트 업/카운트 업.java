import java.util.ArrayList;
import java.util.List;

class Solution {
     public int[] solution(int start_num, int end_num) {
        List<Integer> tempList = new ArrayList<>();
        for (int i = start_num; i <= end_num; i++) {
            tempList.add(i);
        }

        int[] answer = new int[tempList.size()];
        for (int i = 0; i < tempList.size(); i++) {
            answer[i] = tempList.get(i);
        }
        
        return answer;
 
    }
}