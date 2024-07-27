class Solution {
    private int[][] gBoard;
    private int xBound;
    private int yBound;
    private int[] dx = {0, 0, 1, -1, 1, 1, -1, -1};
    private int[] dy = {1, -1, 0, 0, 1, -1, 1, -1};
    
    public int solution(int[][] board) {
        gBoard = board;
        xBound = board.length;
        yBound = board[0].length;
        int answer = 0;
        int newX = 0;
        int newY = 0;
        
        for(int i = 0; i < xBound; i++){
            for(int j = 0; j < yBound; j++){
                if(board[i][j] == 1){
                    for(int k = 0; k < 8; k++){
                        newX = i + dx[k];
                        newY = j + dy[k];
                        if(isExist(newX, newY) && board[newX][newY] != 1){
                            board[newX][newY] = -1;
                        }
                    }
                }
            }
        }
        
        for(int i = 0; i < xBound; i++){
            for(int j = 0; j < yBound; j++){
                if(board[i][j] == 0){
                    answer++;
                }
            }
        }
        
        return answer;
    }
    
    public boolean isExist(int x, int y){
        if(x > xBound - 1 || x < 0 || y > yBound - 1 || y < 0){
            return false;
        }
        
        return true;
    }
}