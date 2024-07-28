// dfs ..?
import java.util.*;

class Solution {
    private static final int NUM_ALPHABETS = 5;
    private String[] alphabets = {"A", "E", "I", "O", "U"};
    private String gWord;
    private int answer = -1;
    private boolean isFound;
    
    public int solution(String word) {
        gWord = word;
        dfs(new StringBuilder());
        return answer;
    }
    
    public void dfs(StringBuilder current){
        answer++;
        if(current.toString().equals(gWord)){
            isFound = true;
            return;
        }
        
        if(current.length() == 5) return;
        
        for(int i = 0; i < NUM_ALPHABETS; i++){
            if(!isFound){
                dfs(current.append(alphabets[i]));
                current.deleteCharAt(current.length() - 1);
            }
        }
    }
}