class Solution {
    private int[] gNumbers;
    private int gTarget;
    private int answer;
    
    public int solution(int[] numbers, int target) {
        gNumbers = numbers;
        gTarget = target;
        
        operation(0, 0);
        
        return answer;
    }
    
    public void operation(int index, int current){
        if(index + 1 == gNumbers.length){
            if(current + gNumbers[index] == gTarget || current - gNumbers[index] == gTarget){
                answer++;
            }
            
            return;
        }
        
        operation(index + 1, current + gNumbers[index]);
        operation(index + 1, current - gNumbers[index]);
    }
}