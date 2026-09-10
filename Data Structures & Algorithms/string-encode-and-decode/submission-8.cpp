class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded = "";
        string x = "";

        for(string s: strs){
            int length = s.size();
            x = to_string(length) + "@" + s;
            encoded += x;
        }
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> answer;
        int l = 0;

        while(l < s.size()){
           for(int i = l + 1; i < s.size(); i++){
                if (s[i] == '@'){
                    int size = stoi(s.substr(l, i - l));
                    answer.push_back(s.substr(i+1, size));
                    l = i + size + 1;
                    break;
                }
           }

        }

        return answer;
    }
};
