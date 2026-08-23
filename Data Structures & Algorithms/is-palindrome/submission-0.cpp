class Solution {
public:
    bool isPalindrome(string s) {
    string x = "";
    string y = "";
    for (int i=0 ; i<s.size() ; i++){
        if(isalnum(s[i])){
            x.push_back(tolower(s[i]));
        }
      }
    
    for(int i = x.size() - 1; i >= 0; i--){
        y.push_back(x[i]);
    }
   return x == y;
    }
};
