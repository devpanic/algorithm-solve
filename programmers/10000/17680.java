import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        if(cacheSize == 0){
            return cities.length * 5;
        }
        
        HashSet<String> citySet = new HashSet<>();
        Queue<String> cityQueue = new LinkedList<>();
        int answer = 0;
        String lowCase = "";
        
        for(int i = 0; i < cities.length; i++){
            lowCase = cities[i].toLowerCase();
            if(citySet.contains(lowCase)){
                cityQueue.remove(lowCase);
                cityQueue.offer(lowCase);
                answer++;
                continue;
            }
            
            if(citySet.size() == cacheSize){
                // 가장 오래된 데이터 제거
                citySet.remove(cityQueue.poll());
            }
            
            citySet.add(lowCase);
            cityQueue.offer(lowCase);
            answer += 5;
        }
        
        return answer;
    }
}