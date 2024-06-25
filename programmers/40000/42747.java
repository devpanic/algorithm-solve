import java.util.*;

class Solution {
    public int solution(int[] citations) {
        if(citations.length == 1){
            return 1;
        }
        
        Arrays.sort(citations);
        int medium = citations.length / 2 - 1;
        int answer = 0;
        int sum = 0;
        
        while(medium <= citations.length){
            for(int i = 0; i < citations.length; i++){
                if(citations[i] >= medium){
                    sum++;
                }
            }
            
            if(medium <= sum){
                answer = medium;
            }
            
            medium++;
            sum = 0;
        }
        
        return answer;
    }
}