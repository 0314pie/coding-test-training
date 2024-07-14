public class Solution {
    public String solution(int[] numLog) {
        StringBuilder result = new StringBuilder();
        
        for (int i = 1; i < numLog.length; i++) {
            int difference = numLog[i] - numLog[i - 1];
            switch (difference) {
                case 1:
                    result.append('w');
                    break;
                case -1:
                    result.append('s');
                    break;
                case 10:
                    result.append('d');
                    break;
                case -10:
                    result.append('a');
                    break;
                default:
                    // handle unexpected difference if needed
                    break;
            }
        }
        
        return result.toString();
    }
}