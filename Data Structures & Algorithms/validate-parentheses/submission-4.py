class Solution:
    def isValid(self, s: str) -> bool:
        s=s.strip()
        length = len(s)
        mid = length//2
        if (length%2==1):
            return False
        stack=[]
        char_map = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i not in char_map:
                stack.append(i)
            else: 
                supposed_char = char_map[i]
                if len(stack)==0: return False
                if (stack[-1]==supposed_char):
                    stack.pop()
                else: return False
        if len(stack)>0: return False
        return True

        