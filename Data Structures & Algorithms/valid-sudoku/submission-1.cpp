class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for(int r = 0; r < 9; r++){
            unordered_set<int> row_duplicate;
            for(int c = 0; c < 9; c++){
                if(board[r][c] == '.'){
                    continue;
                }
                if(row_duplicate.find(board[r][c]) == row_duplicate.end()){
                    row_duplicate.insert(board[r][c]);
                }
                else{
                    return false;
                }
            }
        }

         for(int c = 0; c < 9; c++){
            unordered_set<int> column_duplicate;
            for(int r = 0; r < 9; r++){
                if(board[r][c] == '.'){
                    continue;
                }
                if(column_duplicate.find(board[r][c]) ==column_duplicate.end()){
                    column_duplicate.insert(board[r][c]);
                }
                else{
                    return false;
                }
            }
        }


        for(int r = 0; r < 9; r += 3){
            for(int c = 0; c < 9; c += 3){
                unordered_set<int> duplicates;
                    for(int sr = r; sr < r+ 3; sr++){
                        for(int sc = c; sc < c + 3; sc ++){
                                if(board[sr][sc] == '.'){
                                    continue;
                                }   
                              if(duplicates.find(board[sr][sc]) == duplicates.end()){
                                    duplicates.insert(board[sr][sc]);
                                }
                                else{
                                    return false;
                                }

                        }
                    }
            }
        }

        return true;
    }
};
