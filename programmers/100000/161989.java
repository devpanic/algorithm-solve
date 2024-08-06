class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 1;
        int max = section[0] + m - 1;
        
        for(int i = 1; i < section.length; i++){
            if(section[i] > max){
                max = section[i] + m - 1;
                answer++;
            }    
        }
        
        return answer;
    }
}