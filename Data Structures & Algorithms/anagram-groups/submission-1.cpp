class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> name;
        vector<vector<string>> answer;


        for(int i = 0; i < strs.size(); i++){
            string x = strs[i];
            sort(x.begin(), x.end());
          
            name[x].push_back(strs[i]);
        }
        
        for(auto& pair: name){
            answer.push_back(pair.second);
        }
        return answer;
    }
};
