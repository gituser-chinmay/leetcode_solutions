class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #In this solution, each element in the array is replaced with
        #the max sum that can be made till that array
        #Ex - [2,1,-3]
        #In first iteration, array is [3,-3]
        max = nums[0]
        
        for i in range(1, len(nums)):
            #Replacing element with max sum up till that index
            if nums[i] + nums[i-1] > nums[i]:
                nums[i] = nums[i] + nums[i-1]
            #Re defining max to the greatest value
            if nums[i] > max:
                max = nums[i]
                
        return max
