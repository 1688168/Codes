##############
# 20240217
##############
class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        left2right={
            "{":"}",
            "[":"]",
            "(":")"
        }
        for cc in s:
            if cc in ['{', '[', '(']:
                stk.append(cc)
            else:
                if not stk or cc != left2right[stk[-1]]:
                    return False
                stk.pop()
        return True if not stk else False
        

##############
# 20231230
##############
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if stk:
                if (c == ")" and stk[-1] == "(") or (c == "]" and stk[-1] == "[") or (c == "}" and stk[-1] == "{"):
                    stk.pop()
                    continue
            stk.append(c)

        return not stk


##############
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif c in [')', ']', '}']:
                if len(stack) == 0:
                    return False
                elif c == ')' and stack[-1] != '(':
                    return False
                elif c == ']' and stack[-1] != '[':
                    return False
                elif c == '}' and stack[-1] != '{':
                    return False
                else:
                    pass
                stack.pop()
        return True if len(stack) == 0 else False
