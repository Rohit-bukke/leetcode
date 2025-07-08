import java.util.HashSet;

public class Solution{
    public boolean containsDuplicate(int[] nums){
        //create a hashset to store elements form the array
        HashSet<Integer> seennumber = new HashSet<>();

        //Interating through each number in the array
        for(int num: nums){
            //check if element is repeated or not
            if(seennumber.contains(num)){
                return true;
            }
           //Addding the element to the hashset
           seennumber.add(num);
        }
       return false; //No duplicates found in the array 
    }
}
