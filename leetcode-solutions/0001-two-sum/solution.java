public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for(int i=0; i<nums.length; i++){

            int complement = target - nums[i];

            if(map.containsKey(complement)){
                return new int[] {map.get(complement),i};
            }

            //otherwisse we add the into the Hashmap

            map.put(nums[i],i);
            
        }
        //return an empty array if the solution is not found
        return new int[] {};
    }
}
