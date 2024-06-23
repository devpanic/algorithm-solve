import java.util.Stack;

class Solution
{
    public int solution(String s)
    {
        char[] input = s.toCharArray();
        Stack<Character> continuous = new Stack<Character>();
        
        for(int i = 0; i < input.length; i++){
            if(continuous.empty()){
                continuous.push(input[i]);
                continue;
            }
            
            if(continuous.peek() == input[i]){
                continuous.pop();
            } else {
                continuous.push(input[i]);
            }
        }
        
        if(continuous.empty()){
            return 1;
        }
        
        return 0;
    }
}