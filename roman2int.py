class Solution:
    def romanToInt(self, s: str) -> int:
        """
        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.
        :param s:
        :return:
        """
        rom_int_map = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        int_rom_map = {1: 'I', 5: 'V', 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        for k in rom_int_map.keys():
            if s.count(k):
                print(f"Roman number {k} occur {s.count(k)} times")
                r = rom_int_map[k] * s.count(k)
        return r



test_cases = ["III", "LVIII", "MCMXCIV"]
simple_case = ["III"]

test = Solution()
for t in simple_case:
    result = test.romanToInt(t)
    print(result)