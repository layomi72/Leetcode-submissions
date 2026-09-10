class Solution {
public:
    bool isAnagram(string s, string t) {
        string s1 = "";
        string t1 = "";

        for (int i = 0; i < s.size(); i++){
            if (isalnum(s[i])){
                s1 += tolower(s[i]);
            }
        }

          for (int i = 0; i < t.size(); i++){
            if (isalnum(t[i])){
                t1 += tolower(t[i]);
            }
        }
   
        
        sort(s1.begin(), s1.end());
        sort(t1.begin(), t1.end());

      return s1 == t1;
    }
};
