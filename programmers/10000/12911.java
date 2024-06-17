class Solution {
    public int solution(int n) {
        int orgTrueBits = Integer.bitCount(n);
        
        while(true){
            if(orgTrueBits == Integer.bitCount(++n)){
                return n;
            }    
        }
    }
}