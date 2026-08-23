class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] answer = new int[2];
        for (int i = 0; i<numbers.length ; i++){
            for (int j = 1; j<numbers.length ; j++){
                if (numbers[i] + numbers[j] == target && i<j){
                    answer[0] = i+1;
                    answer[1] = j+1;
                }
            }
        }
        return answer;
    }
}
