import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Comparator.reverseOrder());
        int standard = priorities[location];
        
        for(int priority: priorities){
            priorityQueue.add(priority);
        }
        
        int answer = 0;
        
        while(!priorityQueue.isEmpty()){
            for(int i = 0; i < priorities.length; i++){
                if(priorityQueue.peek() == priorities[i]){
                    priorityQueue.poll();
                    answer++;
                    
                    if(location == i){
                        return answer;
                    }
                }
            }
        }
        
        return answer;
    }
}