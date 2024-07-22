class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = my_string;
        for (int[] query : queries) {
            int s = query[0];
            int e = query[1];
            String reverse_string = "";
            for (int i = e; i >= s; i--) {
                reverse_string += answer.charAt(i);
            }
            answer = answer.substring(0, s) + reverse_string + answer.substring(e + 1);
        }
        return answer;
    }
}