import java.lang.Math;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int solution(int[] arr) {
        int answer = arr[0];
        
        int numA = -1;
        int numB = -1;
        int temp = 0;
        
        for(int i = 1; i < arr.length; i++){
            numA = answer;
            numB = arr[i];
            // 유클리드 호제법
            while(true){
                if(numA % numB != 0){
                    temp = numB;
                    numB = numA % numB;
                    numA = temp;
                } else {
                    break;
                }
            }
            
            // 두수의 곱(numB) / 최대공약수
            answer = arr[i] * answer / numB;
        }
        
        return answer;
    }
}