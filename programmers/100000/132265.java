// map으로 풀었으면 더 간단했을것 같다

import java.util.*;

class Solution {
    public int solution(int[] topping) {
        Set<Integer> firstSet = new HashSet<>();
        Set<Integer> secondSet = new HashSet<>();
        int toppingLength = topping.length;
        int answer = 0;
        boolean isContain = false;
        
        for(int i = 1; i < toppingLength; i++){
            secondSet.add(topping[i]);
        }
        
        for(int i = 0; i < toppingLength; i++){
            firstSet.add(topping[i]);
            
            for(int j = i + 1; j < toppingLength; j++){
                if(topping[i] == topping[j]){
                    isContain = true;
                    break;
                }
            }
            
            if(!isContain){
                secondSet.remove(topping[i]);
            }
            
            if(firstSet.size() == secondSet.size()){
                answer++;
            }
            
            isContain = false;
        }
        
        return answer;
    }
}