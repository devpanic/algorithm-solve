import java.util.*;

class Solution {
    public int solution(int[] elements) {
        int sum = 0;
        int unit = 1;
        int limit = elements.length;
        Set<Integer> sums = new HashSet<>();
        
        while(unit != limit){
            for(int i = 0; i < limit; i++){
                for(int j = i; j < i + unit; j++){
                    sum += elements[j % limit];
                }
                sums.add(sum);
                sum = 0;
            }
            unit++;
        }
        
        return sums.size() + 1;
    }
}