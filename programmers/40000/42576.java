import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> participants = new HashMap<>();
        
        for(String participantPerson : participant){
            participants.put(participantPerson, participants.getOrDefault(participantPerson, 0) + 1);
        }
        
        int count = 0;
        
        for(String complete : completion){
            count = participants.get(complete);
            if(count == 1){
                participants.remove(complete);
                continue;
            }
            
            participants.put(complete, count - 1);
        }
        
        return participants.keySet().iterator().next();
    }
}