class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        int[] tempArr = new int[intStrs.length];
        int count = 0;

        for (String str : intStrs) {
            String answer = "";
            for (int i = s; i < s + l; i++) {
                answer += str.charAt(i);
            }
            int a = Integer.parseInt(answer);
            if (a > k) {
                tempArr[count++] = a;
            }
        }
        
        int[] answerArr = new int[count];
        System.arraycopy(tempArr, 0, answerArr, 0, count);
        
        return answerArr;
    }
}