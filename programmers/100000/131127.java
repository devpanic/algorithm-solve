import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        int dateLimit = discount.length - 9;
        HashMap<String, Integer> wantMap = new HashMap<>();
        
        for(int i = 0; i < want.length; i++){
            wantMap.put(want[i], number[i]);    
        }
        
        HashMap<String, Integer> copied = new HashMap<>();
        int temp = 0;
        // 윈도우 설정
        for(int days = 0; days < dateLimit; days++){
            copied.putAll(wantMap);
            for(int rotate = days; rotate < days + 10; rotate++){
                if(copied.containsKey(discount[rotate])){
                    temp = copied.get(discount[rotate]);
                    temp--;
                    if(temp == 0){
                        copied.remove(discount[rotate]);
                    } else {
                        copied.put(discount[rotate], temp);
                    }
                }
                
            }
            
            if(copied.keySet().size() == 0){
                answer++;
            }
        }
        
        return answer;
    }
}