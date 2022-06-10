class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i in range(len(s)):
            if s[i] == "#" and len(stack1)>0:
                stack1.pop()
            elif s[i] == "#" and len(stack1)==0:
                stack1.append("")
            else:
                stack1.append(s[i])
        for i in range(len(t)):
            if t[i] == "#" and len(stack2)>0:
                stack2.pop()
            elif t[i] == "#" and len(stack2)==0:
                stack2.append("")
            else:
                stack2.append(t[i])
        stack1 = "".join(stack1)
        stack2 = "".join(stack2)
        return stack1 == stack2