class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for item in s:
            if item=='*':
                if len(stack)>0:
                    stack.pop()
            else:
                stack.append(item)
        return "".join(stack)                    
            
        