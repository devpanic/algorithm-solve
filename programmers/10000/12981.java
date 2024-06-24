import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        Set<String> dict = new HashSet<String>();
        String before = words[0];
        dict.add(words[0]);
        
        for(int i = 1; i < words.length; i++){
            if(before.charAt(before.length() - 1) != words[i].charAt(0)){
                answer[0] = i % n + 1;
                answer[1] = i / n + 1;
                return answer;
            }
            
            dict.add(words[i]);
            
            if(dict.size() != (i + 1)){
                answer[0] = i % n + 1;
                answer[1] = i / n + 1;
                return answer;
            }
            
            before = words[i];
        }
        
        return answer;
    }
}