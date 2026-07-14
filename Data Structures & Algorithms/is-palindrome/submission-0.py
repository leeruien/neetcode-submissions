class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = s.replace(" ", "")
        new = cleaned.lower()
        length = len(cleaned)
        end = length - 1
        start = 0
        while end >= start:
            if not ((new[start]).isalnum()):
                start+=1
                continue
            if not ((new[end]).isalnum()):
                end-=1
                continue
            if new[end]!=new[start]:
                return False
            else:
                start+=1
                end-=1
        return True


            
