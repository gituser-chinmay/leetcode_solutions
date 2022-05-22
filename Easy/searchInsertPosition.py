class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #Binary search solution - a left pointer and right pointer is used to locate target
        l = 0
        r = len(nums)-1
            
        while l<=r:
            #Search for the middle index of sorted array
            mid = l + (r-l)//2
            
            #Return the index if target is found
            if nums[mid]==target:
                return mid
            
            #If the element at index is greater than target, the right pointer is
            #moved to one index behind the mid index
            if nums[mid] > target:
                r = mid - 1
                
            #Else the left pointer is moved one index ahead of mid
            elif nums[mid] < target:
                l = mid + 1
        
        #The pointer with a greater index value denotes the index position of the
        #target element
        if l>r:
            return l
        elif r>l:
            return r

            
