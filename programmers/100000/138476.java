import java.util.*;

class Solution {
    public int solution(int k, int[] tangerines) {
        HashMap<Integer, Integer> tangerineMap = new HashMap<>();
        
        for(int tangerine: tangerines){
            tangerineMap.put(tangerine, tangerineMap.getOrDefault(tangerine, 0) + 1);
        }
        
        List<Integer> sortedTangerine = new ArrayList<Integer>(tangerineMap.values());
        sortedTangerine.sort((tangerine1, tangerine2) -> tangerine2 - tangerine1);
        
        int answer = 0;
        int sum = 0;
        
        for(Integer tangerine: sortedTangerine){
            sum += tangerine;
            answer++;
            if(sum >= k){
                break;
            }
        }
        return answer;
    }
}