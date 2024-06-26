import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int nextDeploy = 0;
        int jobCount = progresses.length;
        int[] deployDays = new int[jobCount];
        
        for(int i = 0; i < jobCount; i++){
            deployDays[i] = (100 - progresses[i]) / speeds[i] + (((100 - progresses[i]) % speeds[i] == 0) ? 0 : 1);
        }
        
        List<Integer> answer = new ArrayList<>();
        int sum = 0;
        int max = 0;
        for(int i = 0; i < jobCount; i++){
            if(max >=deployDays[i]){
                sum++;
            } else {
                if(sum != 0){
                    answer.add(sum);
                }
                sum = 1;
                max = deployDays[i];
            }
        }
        
        if(sum != 0){
            answer.add(sum);
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}