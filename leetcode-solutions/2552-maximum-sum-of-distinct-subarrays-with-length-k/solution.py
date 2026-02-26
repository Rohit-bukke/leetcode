class Solution:
    def maximumSubarraySum(self, nums, k):
        
        counter = defaultdict(int)
        curr_sum = 0
        left = 0
        ans = 0

        for right in range(len(nums)):
            counter[nums[right]] += 1
            curr_sum += nums[right]

            if right - left + 1 > k:
                counter[nums[left]] -= 1
                curr_sum -= nums[left]
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1

            if right - left + 1 == k and len(counter) == k:
                ans = max(ans, curr_sum)

        return ans
