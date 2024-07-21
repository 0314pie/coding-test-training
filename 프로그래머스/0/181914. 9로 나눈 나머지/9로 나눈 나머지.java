class Solution {
    public int solution(String number) {
        int answer = 0;
        String num[] = number.split("");

        for(String i : num) {
            answer += Integer.parseInt(i);
        }
        return answer % 9;
    }
}