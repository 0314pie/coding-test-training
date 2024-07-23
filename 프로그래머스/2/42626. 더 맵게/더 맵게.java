import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        int cnt = 0;
        
        for (int s : scoville) {
            heap.add(s);
        }
        
        while (true) {
            int a = heap.poll();
            
            if (a >= K) {
                break;  
            }
            

            if (heap.isEmpty()) {
                return -1;
            }
            
            int b = heap.poll();
            int c = a + b * 2;
   
            heap.add(c);
            cnt += 1;
        }
        
        return cnt;
    }
}