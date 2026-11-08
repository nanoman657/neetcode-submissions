class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const uniqueSet = new Set(nums);
        const duplicate = uniqueSet.size < nums.length;
        return duplicate
    }
}
