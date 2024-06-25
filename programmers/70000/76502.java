import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        int length = s.length();
        StringBuilder rotated = new StringBuilder(s);
        char firstChar = ' ';
        for(int i = 0; i < length; i++){
            firstChar = rotated.charAt(0);
            rotated.deleteCharAt(0);
            rotated.append(firstChar);
            answer += isPair(rotated) ? 1 : 0;
        }
        
        return answer;
    }
    
    public boolean isPair(StringBuilder rotated){
        char current = ' ';
        Stack<Character> pairCheck = new Stack<>();
        for(int i = 0; i < rotated.length(); i++){
            switch(rotated.charAt(i)){
                case '[':
                case '(':
                case '{':
                    pairCheck.push(rotated.charAt(i));
                    break;
                case '}':
                    if(pairCheck.isEmpty() || pairCheck.peek() != '{'){
                        return false;
                    }
                    pairCheck.pop();
                    break;
                case ')':
                    if(pairCheck.isEmpty() || pairCheck.peek() != '('){
                        return false;
                    }
                    pairCheck.pop();
                    break;
                case ']':
                    if(pairCheck.isEmpty() || pairCheck.peek() != '['){
                        return false;
                    }
                    pairCheck.pop();
                    break;
            }
        }
        if(pairCheck.isEmpty()){
            return true;
        }
        return false;
    }
}