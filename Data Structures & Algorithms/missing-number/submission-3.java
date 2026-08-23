class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length; // The size of the array
        int ans = 0;

        // XOR all numbers from 0 to n
        for (int i = 0; i <= n; i++) {
            ans ^= i; // XOR all numbers from 0 to n
        }

        // XOR all numbers in the array
        for (int num : nums) {
            ans ^= num; // XOR all numbers in nums
        }

        // The result is the missing number
        return ans;
    }
}

