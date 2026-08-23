class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()){
            return false;
        }
        else{
            std::unordered_map<char, int> frequency;
            for (char i : s){
                frequency[i]++;
            }
            for (char j: t){
                frequency[j]--;
            }
            for (const auto& pair : frequency){
                if (pair.second < 0){
                    return false;
                }
            }
            return true;

        }
}};
