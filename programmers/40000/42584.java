import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        
        Stack<Integer> notFallen = new Stack<>();
        
        for(int i = 0; i < prices.length; i++){
            while(!notFallen.isEmpty() && prices[i] < prices[notFallen.peek()]){
                answer[notFallen.peek()] = i - notFallen.pop();
            }
            
            notFallen.push(i);
        }
        
        while(!notFallen.isEmpty()){
            answer[notFallen.peek()] = prices.length - notFallen.pop() - 1;
        }
        
        return answer;
    }
}