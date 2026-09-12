class Solution {
public:
    int countPrefixSuffixPairs(vector<string>& words) {
        int ans = 0;

        for(int i = 0; i < words.size(); i++){
            for(int j = 1; j < words.size(); j++){
                string str1 = words[i];
                string str2 = words[j];

                if( i < j) {
                    if (str1.size() > str2.size()){
                        continue;
                    }
                    string prefix = str2.substr(0, str1.size());
                    string suffix = str2.substr(str2.size() - str1.size());
                    if(str1 == prefix and str1 == suffix){
                        ans++;
                    }

                }
                    
            }
        }
        return ans;
    }
};