doc = """
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

"""


class Solution:
    def isValid(self, s: str) -> bool:
        brackets = dict(("()", "{}", "[]"))
        open_brackets = "({["
        stack = []
        for br in s:
            if br in open_brackets:
                stack.append(br)
                print(stack, br)
            elif len(stack) == 0 or br != brackets[stack.pop()]:
                return False
        return len(stack) == 0