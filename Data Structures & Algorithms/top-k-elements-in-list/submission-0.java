class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int max_val = 0;
        int remove = 0;
        int[] answer = new int[k];
        int L = 0;
        HashMap<Integer,Integer> frequency = new HashMap<Integer,Integer>();
        for(int i=0; i<nums.length;i++){
            if(frequency.containsKey(nums[i])){
                frequency.put(nums[i],frequency.get(nums[i])+1);
            }
            else{
                frequency.put(nums[i],1);
            }
        }
        while (k>0){
        for(Map.Entry<Integer,Integer> entry: frequency.entrySet()){
            int key = entry.getKey();
            int value = entry.getValue();
    
            if(value>max_val){
                max_val = value;
                remove = key;
            }
        }
        frequency.remove(remove);
        answer[L] = remove;
        L +=1;
        k -=1;
        max_val=0;
        }
        return answer;

    }
}
