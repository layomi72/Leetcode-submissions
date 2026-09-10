class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> frequency;
        vector<int> ans;
        

        for(int i = 0; i < nums.size(); i++){
            frequency[nums[i]]++;
        }
        int count = k;

        while (k > 0) {
            int best = 0;
            int x;
            for(auto& pair: frequency){


                if (pair.second > best){
                    x = pair.first;
                    best = pair.second;
                }


            }
            frequency.erase(x);
            ans.push_back(x);
            k -= 1;

        }
        return ans;
    }
};
