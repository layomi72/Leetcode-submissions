class Solution {
    public int singleNumber(int[] nums) {
        int answer = 0;
        if(nums.length == 1){
            return nums[0];
        }
        else{
            for(int i = 0 ; i < nums.length ; i++){
                answer = answer ^ nums[i];
            }
            return answer;
        }
    }
}
