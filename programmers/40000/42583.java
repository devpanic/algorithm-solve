import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        if(bridge_length == 1) return truck_weights.length + 1;
        if(truck_weights.length == 1) return bridge_length + 1;
        
        Queue<Integer> bridge = new LinkedList<>();
        
        for(int i = 0; i < bridge_length; i++){
            bridge.offer(0);
        }
        
        int answer = 0;
        int currentWeight = 0;
        int currentTruck = 0;
        
        while(currentTruck < truck_weights.length){
            currentWeight -= bridge.poll();
            answer++;
            
            if(currentWeight + truck_weights[currentTruck] <= weight){
                bridge.offer(truck_weights[currentTruck]);
                currentWeight += truck_weights[currentTruck++];
            } else {
                bridge.offer(0);
            }
        }
        
        return answer + bridge_length;
    }
}