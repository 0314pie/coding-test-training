import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
         HashMap<String, Integer> playerMap = new HashMap<>();
        
        for (int i = 0; i < players.length; i++) {
            playerMap.put(players[i], i);
        }
         for (String call : callings) {
            int i = playerMap.get(call);
            
            if (i > 0) { 
                String temp = players[i];
                players[i] = players[i - 1];
                players[i - 1] = temp;
                
                playerMap.put(players[i], i);
                playerMap.put(players[i - 1], i - 1);
            }
        }
        
        return players;
    }

}