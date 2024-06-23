class Solution {
    public String solution(String s) {
        String answer = "";
        int lastSpaceIndex = -1;
        char[] inputCharArr = s.toLowerCase().toCharArray();
        
        for(int i = 0; i < inputCharArr.length; i++){
            if(inputCharArr[i] == ' '){
                lastSpaceIndex = i;
                answer += inputCharArr[i];
                continue;
            }
            
            if(i == lastSpaceIndex + 1){
                answer += Character.toUpperCase(inputCharArr[i]);
                continue;
            }
            
            answer += inputCharArr[i];
        }
        
        return answer;
    }
}