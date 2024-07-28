class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr2[0].length];
        int temp = 0;
        
        for(int i = 0; i < answer.length; i++){
            for(int j = 0; j < answer[0].length; j++){
                for(int k = 0; k < arr2.length; k++){
                    temp += arr1[i][k] * arr2[k][j];
                }        
                
                answer[i][j] = temp;
                temp = 0;
            }
        }
        
        return answer;
    }
}