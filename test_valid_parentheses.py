from Valid_Parentheses import Solution


test_cases = {"()": True, "()[]{}": True, "(]": False, "(){}}{": False}
test = Solution()
for t in test_cases.keys():
    result = test.isValid(t)
    if result == test_cases[t]:
        print(f"test case {t} is PASSED")
    else:
        print(f"test case {t} is FAILED")