class Solution {
    public int[] solution(int n) {
        int temp = n;
        int length = 0;
        
        while (temp != 1) {
            length++;
            if (temp % 2 == 0) {
                temp = temp / 2;
            } else {
                temp = 3 * temp + 1;
            }
        }
        length++; 
        
       
        int[] result = new int[length];
        
   
        int index = 0;
        temp = n;
        
        while (temp != 1) {
            result[index++] = temp;
            if (temp % 2 == 0) {
                temp = temp / 2;
            } else {
                temp = 3 * temp + 1;
            }
        }
        result[index] = 1; 
        
        return result;
    }
}