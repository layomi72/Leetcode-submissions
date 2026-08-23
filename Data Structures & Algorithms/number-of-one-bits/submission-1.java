class Solution {
    public int hammingWeight(int n) {
     int count = 0;
     int temp = n & 1;
     while(n != 0){
        if (temp == 1){
            count += 1;
           n = n >>1;
           temp = n & 1;
        }
        else{
            n = n>>1;
            temp = n & 1;
        }
     }
     return count;
}
}