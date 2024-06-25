import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> closet = new HashMap<>();
        int clothSum = clothes.length;
        
        for(int i = 0; i < clothSum; i++){
            closet.put(clothes[i][1], closet.getOrDefault(clothes[i][1], 0) + 1);
        }
        
        int answer = 1;
        List<Integer> wears = new ArrayList<>(closet.values());
        
        if(wears.size() == 1){
            return clothes.length;
        }
        
        for(int wear : wears){
            answer *= (wear + 1);
        }
        
        return --answer;
    }
}