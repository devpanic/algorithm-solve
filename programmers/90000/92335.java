import java.util.*;

class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        String[] convert = Integer.toString(n, k).split("0");
        String current = "";
        
        for(int i = 0; i < convert.length; i++){
            current = convert[i];
            if(!current.isBlank() && !current.equals("1")){
                answer += isPrime(Long.parseLong(current)) ? 1 : 0;
            }
        }
        
        return answer;
    }
    
    public boolean isPrime(Long num){
        for(int i = 2; i < (int)Math.sqrt(num) + 1; i++){
            if(num % i == 0){
                return false;
            }
        }
        
        return true;
    }
}