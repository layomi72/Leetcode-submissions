class Solution {
    public int[] countBits(int n) {
        int[] no_of_1 = new int[n+1];
        for (int i = 0;i<n+1;i++){
            no_of_1[i] = no(i);
        }
    return no_of_1;
    }
    private int no(int n){
        int count = 0;
        while (n!=0){
            if((n&1) == 1){
                count += 1;
                n = n >> 1;
            }else{
                n = n >> 1;
            }
            
        }
        return count;
    }
}
