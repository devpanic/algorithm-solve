class Solution {
    static int count;
    static boolean[] visited;
    
    public int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];
        dfs(0, k, dungeons);
        return count;
    }
    
    public void dfs(int depth, int life, int[][] dungeons){
        for(int i = 0; i < dungeons.length; i++){
            if(!visited[i] && life >= dungeons[i][0]){
                visited[i] = true;
                dfs(depth + 1, life - dungeons[i][1], dungeons);
                visited[i] = false;
            }
        }
        
        count = Math.max(count, depth);
    }
}