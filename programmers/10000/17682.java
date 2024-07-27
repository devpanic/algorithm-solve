class Solution {
    public int solution(String dartResult) {
        int beforeSum = 0;
        int beforeScore = -1;
        int[] sums = new int[3];
        int sumIndex = -1;
        
        for(int i = 0; i < dartResult.length(); i++){
            switch(dartResult.charAt(i)){
                case 'S':
                    sums[sumIndex] = beforeScore;
                    break;
                case 'D':
                    sums[sumIndex] = twiceScore(beforeScore);
                    break;
                case 'T':
                    sums[sumIndex] = tripleScore(beforeScore);
                    break;
                case '*':
                    sums[sumIndex] *= 2;
                    if(sumIndex > 0) {
                        sums[sumIndex - 1] *= 2;
                    }
                    break;
                case '#':
                    sums[sumIndex] *= -1;
                    break;
                case '0':
                    if(i != 0 && beforeScore == 1){
                        beforeScore = 10;
                    } else {
                        beforeScore = 0;
                        sumIndex++;
                    }
                    break;
                default:
                    beforeScore = dartResult.charAt(i) - '0';
                    sumIndex++;
                    break;
            }
        }
        
        return sums[0] + sums[1] + sums [2];
    }
    
    public int twiceScore(int score){
        return score * score;
    }
    
    public int tripleScore(int score){
        return score * score * score;
    }
}