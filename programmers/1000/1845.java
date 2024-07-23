import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        Map<Integer, Integer> pokemons = new HashMap<>();
        
        for(int i = 0; i < nums.length; i++){
            pokemons.put(nums[i], pokemons.getOrDefault(nums[i], 0) + 1);    
        }
        
        if(nums.length / 2 >= pokemons.keySet().size()){
            return pokemons.keySet().size();
        }
        
        return nums.length / 2;
    }
}