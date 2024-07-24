class Solution {
    public String solution(String[] my_strings, int[][] parts) {
        String answer = "";
        for(int i=0; i < parts.length; i ++){
            int[] part = parts[i];
            String str = my_strings[i];
            int s = part[0];
            int e = part[1];
            
            answer += str.substring(s, e+1);
        }
        
        return answer;
    }
}