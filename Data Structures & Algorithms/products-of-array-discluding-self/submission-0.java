class Solution {
    public int[] productExceptSelf(int[] nums) {
        int product = 1;
        int[] output = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            for(int j =0;j<nums.length;j++){
                if(i == j){
                    product +=0;
                }
                else{
                    product *= nums[j];
                }
            }
            output[i] = product;
            product =1;
        }
        return output;
    }
}  
