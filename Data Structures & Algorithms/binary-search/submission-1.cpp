class Solution {
public:
    int search(vector<int>& nums, int target) {
       int n = nums.size();
       int x = 0;
       int y = nums.size();
       int z = (x + y)/2;
       while(n>0){
        if (nums[z] == target){
            return z;
        }
        else if (nums[z] < target){
            n = n/2;
            x = z;
            z = (x + y)/2;
        }
        else{
             y = z;
             n = n/2;
             z = (x + y)/2;
        }
       }
       return -1;
    }
};
