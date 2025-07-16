class Solution {
    public int maxSubArray(int[] nums) {
        int maxi = Integer.MIN_VALUE;         //int or else long we can use
    
        int sum = 0;
        int n = nums.length;

        for(int i=0; i<n; i++){

            sum += nums[i]; 
        
            if(sum > maxi){
            maxi = sum;
            }

            //if sum is lesser than 0 discard the sum calculated
            if(sum<0){
                sum=0;
            }
        
        }
            
    return maxi;
    }
}
