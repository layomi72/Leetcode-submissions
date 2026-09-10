class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix_product;
        vector<int> suffix_product;
        vector<int> output;


        int x = 0;
        int prefix = 1; 
        for(int i = 0; i < nums.size(); i++){
                prefix_product.push_back(prefix);
                prefix = prefix * nums[i];
        }

        int suffix = 1; 
        for(int i = nums.size() - 1; i > -1 ; i--){
            suffix_product.push_back(suffix);
            suffix = suffix * nums[i];
        }

        // reverse suffix_product then mulitple prefix and suffix to get the answer of both
        reverse(suffix_product.begin(), suffix_product.end());

        for(int i = 0; i < suffix_product.size(); i++){
            output.push_back(prefix_product[i] * suffix_product[i]);
        }

        return output;
    }
};
