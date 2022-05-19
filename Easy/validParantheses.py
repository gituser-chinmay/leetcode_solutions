class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        i=0
        j=i
        while True:
            #Keep appending consecutive character from s into the stack
            if i<len(s):
                stack.append(s[i])
            else:
                break
            
            #The first element of the string cannot be compared to check for valid parenhteses
            #So starting from second element
            #Comparing the last and second last element of stack, if they are matching parantheses the matching set 
            #elements are removed from stack
            if i!=0 and self.validity(stack[j-1], stack[j]):
                stack.pop()
                stack.pop()
                
            i+=1
            #The size of stack variable keep changing when an matching pair is removed
            #Since the last and second last elements of stack are always compared, variable value is taken 
            #as length of the stack
            j=len(stack)
            
        #If there are any elements remaining in stack, that means a matching parantheses was not found for one
        #or more pairs
        if len(stack)==0:
            return True
        else:
            return False
        
    def validity(self, a, b):
        if a=='(' and b==')':
            return True
        elif a=='[' and b==']':
            return True
        elif a=='{' and b=='}':
            return True
        else:
            return False