class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        unordered_set<string> answer;

        for(int i = 0; i < words.size(); i++){
            for(int j = 0; j < words.size(); j++){
                if(i != j and words[j].find(words[i]) != string::npos){
                    answer.insert(words[i]);
                }
            }
        }
        return vector<string>(answer.begin(), answer.end());
    }
};