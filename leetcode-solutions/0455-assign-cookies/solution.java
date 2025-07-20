class Solution {
    public int findContentChildren(int[] greed, int[] size) {
        int n = greed.length;
        int m= size.length;
        int l=0;
         int r=0;
        Arrays.sort(greed);
        Arrays.sort(size);
        
        while (l<m && r<n){
            if(greed[r]<= size[l]){
                r= r+1;
            }
        l=l+1;
        }
    return r;
    }
}
