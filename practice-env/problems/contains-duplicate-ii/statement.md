# Contains Duplicate II

Given an integer array `nums` and an integer `k`, return `true` if there are two **distinct** indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`. Otherwise, return `false`.

**Example 1:**
- Input: `nums = [1, 2, 3, 1], k = 3`
- Output: `true`
- Explanation: `nums[0] == nums[3]` and `|0 - 3| = 3 <= 3`.

**Example 2:**
- Input: `nums = [1, 0, 1, 1], k = 1`
- Output: `true`
- Explanation: `nums[2] == nums[3]` and `|2 - 3| = 1 <= 1`.

**Example 3:**
- Input: `nums = [1, 2, 3, 1, 2, 3], k = 2`
- Output: `false`
- Explanation: Every pair of equal values is more than 2 indices apart.

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= 10^5`
