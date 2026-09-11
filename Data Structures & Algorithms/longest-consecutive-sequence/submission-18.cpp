class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int>nums_set(nums.begin(), nums.end());
        if (nums.size() == 0){
            return 0;
        }
        int best = 1;

        
        for(int num: nums_set){
            int count = 1;
            if(nums_set.find(num - 1) != nums_set.end()){
                continue;
            }
            num++;
            while(nums_set.find(num) != nums_set.end()){
                count++;
                best = max(count,best);
                num++;
                }
    }
        return best;
 }
};
