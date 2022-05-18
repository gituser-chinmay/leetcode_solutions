def longestCommonPrefix(self, strs: List[str]) -> str:
        #The first word is chosen to compare remaining words
        prefix = strs[0]
        
        for s in strs:
            #The prefix is compared with te other words in list. In the first iteration, no changes happen
            #as the second condition is not satisfied
            while prefix and not s.startswith(prefix):
                
                #If the word does not start with the prefix, the prefix is manipulated so that
                #the last letter of the prefix is removed, and so on all the words are checked for longest occurring prefix
                prefix = prefix[:-1]
        
        return prefix
