class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i=0;i < nums.size();i++){
            for(int j=0;j< nums.size();j++){
                if(nums[i]+ nums[j] == target && i!=j && i<j){
                    std::vector<int> list;
                    list.push_back(i);
                    list.push_back(j);
                    return list;
                }
                else if(nums[i]+ nums[j] == target && i!=j && j<i){
                    std::vector<int> list;
                    list.push_back(j);
                    list.push_back(i);
                    return list;
                }
            }
        }
    }
};
