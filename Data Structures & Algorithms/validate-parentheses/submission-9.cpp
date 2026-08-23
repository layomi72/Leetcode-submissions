class Solution {
public:
    bool isValid(string s) {
        stack<char> stck;
        if(s.size() % 2 != 0 || s[0] == '}' || s[0] == ']' || s[0] == ')'){
            return false;
        }
        for (int i = 0;i<s.size();i++){
            if(s[i] == '(' || s[i] == '{' || s[i] == '['){
                stck.push(s[i]);
            }
            else if(stck.empty()){
                return false;
            }
            else if( s[i] == ')' && stck.top() == '('){
                stck.pop();
            }
            else if( s[i] == '}' && stck.top() == '{'){
                stck.pop();
            }
            else if( s[i] == ']' && stck.top() == '['){
                stck.pop();
            }
            else{
                return false;
            }
            
        }
        if (stck.empty()){
            return true;
        }
        else{
            return false;
        }
    }
};