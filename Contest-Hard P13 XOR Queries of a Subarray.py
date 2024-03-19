class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {
        int [] result=new int[queries.length];
        for(int i=0;i<queries.length;i++){
            int n=arr[queries[i][0]];
            for(int j=queries[i][0]+1;j<queries[i][1]+1;j++){
                n=n^arr[j];
            }
            result[i]=n; 
        }
        return result;
        
    }
}
