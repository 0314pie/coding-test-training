class Solution {
    public String solution(String my_string, int m, int c) {
        int l = my_string.length();
        int row = (l + m - 1) / m;
        
        char arr[][] = new char[row][m];
        
        int index =0;
        for(int i = 0; i < row; i ++){
            for(int j = 0; j < m; j ++){
                if(index < l){
                    arr[i][j] =  my_string.charAt(index);
                    index ++;
                }
            }
        }
        
        char[] result = new char[row];
        for (int i = 0; i < row; i++) {
            result[i] = arr[i][c-1];
        }
        
        return new String(result).replaceAll(" ", "");
    }
}