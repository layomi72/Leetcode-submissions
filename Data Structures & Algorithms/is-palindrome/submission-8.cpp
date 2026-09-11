class Solution {
public:
    bool isPalindrome(string s) {
        string sforward = "";
        string sreverse = "";

        for(char c: s){
            if( isalnum(c)){
                sforward += tolower(c);
            }
        }
        sreverse = sforward;
        reverse(sreverse.begin(), sreverse.end());

        return sforward == sreverse;
        
        
    }
};
