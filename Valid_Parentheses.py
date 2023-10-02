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
        open = {"(": 0, "[": 1, "{": 2}
        closed = {0: ")", 1: "]", 2: "}"}
        for brackets in open.keys():
            if s.find(brackets):
                if s.find(closed[open[brackets]]):
                    open_bracket_index = s.index(brackets)
                    closed_bracket_index = s.index(closed[open[brackets]])
                    if closed_bracket_index - open_bracket_index == 1:
                        return True
                    else:
                        return False


test_case = "()[]{}"

test = Solution()
print(test.isValid("[]"))