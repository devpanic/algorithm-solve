import java.util.*;

class Solution {
    public int solution(String str1, String str2) {
        if(str1.length() == 0 || str2.length() == 0){
            return 1;
        }
        
        // 1. 두 개씩 문자열 끊어내기
        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();
        
        HashMap<String, Integer> firstStr = new HashMap<>();
        HashMap<String, Integer> secondStr = new HashMap<>();
        double sum = 0;
        double duplicate = 0;
        
        for(int i = 0; i < str1.length() - 1; i++){
            if(isOnlyEng(str1.substring(i, i+2))){
                firstStr.put(str1.substring(i, i + 2), firstStr.getOrDefault(str1.substring(i, i + 2), 0) + 1);
            }
        }
        
        for(int i = 0; i < str2.length() - 1; i++){
            if(isOnlyEng(str2.substring(i, i+2))){
                secondStr.put(str2.substring(i, i + 2), secondStr.getOrDefault(str2.substring(i, i + 2), 0) + 1);
            }
        }
        
        if(firstStr.size() == 0 && secondStr.size() == 0){
            return 1 * 65536;
        }
        
        // 2. 합집합 구하기
        for(int firstValue: firstStr.values()){
            sum += firstValue;
        }
        
        for(String second : secondStr.keySet()){
            if(!firstStr.containsKey(second)){
                sum += secondStr.get(second);
                continue;
            }
            
            if(firstStr.get(second) < secondStr.get(second)){
                sum -= firstStr.get(second);
                sum += secondStr.get(second);
            }
        }
        
        // 3. 교집합 구하기
        for(String first : firstStr.keySet()){
            if(secondStr.containsKey(first)){
                duplicate += Math.min(firstStr.get(first), secondStr.get(first));
            }
        }
        
        if(duplicate == 0){
            return 0;
        }
        
        return (int)((duplicate / sum) * 65536);
    }
    
    public boolean isOnlyEng(String str){
        return str.replaceAll("[^a-zA-Z]", "").length() == str.length();
    }
}