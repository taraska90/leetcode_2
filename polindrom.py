class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_from = list(str(x))
        mediana = len(list_from) // 2
        list_reverse = list_from.copy()
        list_reverse.reverse()
        for i in range(mediana):
            if list_from[i] != list_reverse[i]:
                return False
            else:
                pass
        return True


test_cases = [121, -121 ,10]
t = Solution()
for x in test_cases:
    print(t.isPalindrome(x))

