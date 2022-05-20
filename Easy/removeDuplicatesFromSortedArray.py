class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Faster method compared to O(n^2)
        j = 0
        
        #Compare consecutive elements of list
        #If they are equal, do nothing and increment i keeping j same
        for i in range(1,len(nums)):
            if nums[j]!=nums[i]:
                #Increment j to the next index
                j+=1
                #Replace jth element with ith elemetn, the jth element will be a duplicate of 
                #another element in the list since it was skipped on the condition that
                #jth element adn ith element are equal
                nums[j] = nums[i]
        
        #Since j start from 0 and atleast one unique element is present in the list, return j+1
        return j+1