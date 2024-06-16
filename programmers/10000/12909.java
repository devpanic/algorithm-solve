class Solution {
    boolean solution(String s) {
        int balance = 0;
        char[] inputChars = s.toCharArray();
        for(char inputChar : inputChars){
            if(inputChar == '('){
                balance++;
                continue;
            } else {
                if(--balance < 0) return false;
            }
        }

        if(balance != 0) return false;
        return true;
    }
}