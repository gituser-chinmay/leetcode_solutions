class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        for i in range(len(digits)):
            #Calculating the integer using the power of 10's place of the digit
            sum += digits[i]*10**(len(digits)-1-i)
            
        sum+=1
        num_list = []
        
        #The following loop breaks up the sum integer into ondividual digits, the mod of sum with 10
        #gives the digit at 10**0th place in first iteration
        #Saving those digits in a list and returning reverse of list gives list required
        while True:
            if sum == 0:
                break
            
            num = sum%10                
            sum = sum//10
            num_list.append(num)

        return num_list[len(num_list)-1::-1]
