import java.util.*;

class Solution {
    class Node {
        private int x;
        private int y;
        private int depth;
        
        public Node(int x, int y, int depth){
            this.x = x;
            this.y = y;
            this.depth = depth;
        }
        
        public int getX(){
            return x;
        }
        
        public int getY(){
            return y;
        }
        
        public int getDepth(){
            return depth;
        }
    }
    private int[][] gMaps;
    private boolean[][] visited;
    private int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    private int answer = -1;
    
    public int solution(int[][] maps) {
        gMaps = maps;
        visited = new boolean[gMaps.length][gMaps[0].length];
        
        bfs(0, 0);
        
        return answer;
    }
    
    public void bfs(int x, int y){
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(0, 0, 1));
        visited[0][0] = true;
        
        Node current = null;
        int nextX = 0;
        int nextY = 0;
        
        while(!queue.isEmpty()){
            current = queue.poll();
            
            if(current.getX() == gMaps.length - 1 && current.getY() == gMaps[0].length - 1){
                answer = current.getDepth();
                return;
            }
            
            for(int i = 0; i < 4; i++){
                nextX = current.getX() + directions[i][0];
                nextY = current.getY() + directions[i][1];
                
                if(nextX <= gMaps.length - 1 && nextX >= 0 && nextY <= gMaps[0].length - 1 && nextY >= 0 && gMaps[nextX][nextY] != 0 && !visited[nextX][nextY]){
                    visited[nextX][nextY] = true;
                    queue.add(new Node(nextX, nextY, current.getDepth() + 1));
                }
            }
        }
    }
}