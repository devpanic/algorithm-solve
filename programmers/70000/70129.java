class Solution {
    public int[] solution(String s) {
        int tempLength = -1;
        int rotation = 0;
        int zeroCnt = 0;
        
        while(!s.equals("1")){
            tempLength = s.length();
            // 1. remove zero
            s = s.replaceAll("0", "");
            zeroCnt += tempLength - s.length();
            // 2. transfer length to binary
            s = toBinary(s.length());
            rotation++;
        }
        
        int[] answer = {rotation, zeroCnt};
        return answer;
    }
    
    public String toBinary(int beforeLength){
        String after = "";
        
        while(beforeLength != 0){
            if(beforeLength % 2 == 0){
                after += "0";
            } else {
                after += "1";
            }
            
            beforeLength /= 2;
        }
        
        return after;
    }
}