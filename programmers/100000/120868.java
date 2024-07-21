class Solution {
    public int solution(int[] sides) {
        int max = sides[0] > sides[1] ? sides[0] : sides[1];
        int min = sides[0] > sides[1] ? sides[1] : sides[0]; 
        int total = sides[0] + sides[1];
        int answer = 0;
        
        for(int i = 1; i < total; i++){
            if(i > max && i < max + min){
                answer++;
                continue;
            }
            
            if(max < i + min){
                answer++;
            }
        }
        return answer;
    }
}