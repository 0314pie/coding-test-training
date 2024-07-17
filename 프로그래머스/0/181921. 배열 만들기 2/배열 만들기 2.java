import java.util.ArrayList;
public class Solution {
    public int[] solution(int l, int r) {
        ArrayList<Integer> result = new ArrayList<>();
        
        for (int i = l; i <= r; i++) {
            String str = Integer.toString(i);
            boolean isValid = true;
            for (char c : str.toCharArray()) {
                if (c != '0' && c != '5') {
                    isValid = false;
                    break;
                }
            }
            if (isValid) {
                result.add(i);
            }
        }
        
        if (result.isEmpty()) {
            return new int[]{-1};
        }
        
        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        
        return answer;
    }
}