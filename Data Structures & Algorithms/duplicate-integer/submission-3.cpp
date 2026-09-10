class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> duplicate; 
        for(int i = 0; i < nums.size(); i++ ){
            if (duplicate.find(nums[i]) == duplicate.end())
                duplicate.insert(nums[i]);

            else{
                return true;
            }

        }
            return false;
    }

};