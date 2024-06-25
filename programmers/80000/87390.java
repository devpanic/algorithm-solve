class Solution {
    public int[] solution(int n, long left, long right) {
        int range = (int)right - (int)left + 1;
        int[] answer = new int[range];
        int rest = 0; 
        int mult = 0;
        int max = 0;
        
        long current = 0;
        for(int i = 0; i < range; i++){
            current = left + (long)i;
            rest = (int)(current % n);
            mult = (int)(current / n);
            max = rest > mult ? rest : mult;
            answer[i] = max + 1;
        }
        
        return answer;
    }
}