import java.util.Arrays;

class Solution {
    public String solution(String s) {
        int[] inputNums = Arrays.stream(s.split(" ")).mapToInt(Integer::parseInt).toArray();
        int min = inputNums[0];
        int max = inputNums[0];
        
        for(int inputNum : inputNums){
            if(inputNum > max){
                max = inputNum;
                continue;
            }
            
            if(inputNum < min){
                min = inputNum;
                continue;
            }
        }
        return min + " " + max;
    }
}