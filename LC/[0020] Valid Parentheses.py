class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif c in [')',']','}']:
                if len(stack) == 0:
                    return False
                elif c == ')' and stack[-1] != '(': return False
                elif c==']' and stack[-1] != '[': return False
                elif c=='}' and stack[-1] != '{': return False
                else:
                    pass
                stack.pop()
        return True if len(stack)==0 else False

        
