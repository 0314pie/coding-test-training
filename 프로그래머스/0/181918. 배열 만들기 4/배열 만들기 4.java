class Solution {
    public int[] solution(int[] arr) {
        int[] stk = new int[arr.length];
        int idx = 0;
    
        int i = 0;
        while (i < arr.length) {
            if (idx == 0) {
                stk[idx] = arr[i];
                idx++;
                i++;
            } else if (stk[idx - 1] < arr[i]) {
                stk[idx] = arr[i];
                idx++;
                i++;
            } else {
                idx--;
            }
        }

        int[] finalResult = new int[idx];
        System.arraycopy(stk, 0, finalResult, 0, idx);
        
        return finalResult;

    }
}
