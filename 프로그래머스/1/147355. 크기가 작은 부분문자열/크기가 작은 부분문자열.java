class Solution {
    public int solution(String t, String p) {
        int cnt = 0;
        int len = p.length();
        Long q = Long.parseLong(p);
        
        for(int i=0; i <= t.length() - len ;i++){
            Long a = Long.parseLong(t.substring(i, i+len));
            
            if (a <= q) cnt ++;
        }
        
        return cnt;
    }
}