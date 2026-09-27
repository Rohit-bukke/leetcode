class Solution(object):
    def reverseParentheses(self, s):
        stack = []

        for ch in s:
            if ch == ')':
                temp = []

                # Take everything until '('
                while stack[-1] != '(':
                    temp.append(stack.pop())

                # Remove '('
                stack.pop()

                # temp is already reversed
                stack.extend(temp)

            else:
                stack.append(ch)

        return ''.join(stack)