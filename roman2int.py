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
        # int_rom_map = {1: 'I', 5: 'V', 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        b = 0
        for k in rom_int_map.keys():
            if s.count(k):
                print(f"Roman number {k} occur {s.count(k)} times")
                r = rom_int_map[k] * s.count(k)
                b = b + r
        return int(b)

    def specialCase(self, s: str):
        rom_int_map = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        special_cases = dict(IV=4, IX=9, XL=40, XC=90, CD=400, CM=900)
        b = 0
        for k in special_cases.keys():
            if s.count(k):
                print(f"Roman number {k} occur {s.count(k)} times")
                r = special_cases[k] * s.count(k)
                b = b + r
                s = s.replace(k, '')
        c = 0
        for a in rom_int_map:
            if s.count(a):
                g = rom_int_map[a] * s.count(a)
                c = c + g
        res = c + b
        return int(res)





test_cases = ["III", "LVIII", "MCMXCIV"]
simple_case = ["LVIII"]

test = Solution()
result = test.specialCase(test_cases[2])
print(result)

#for t in simple_case:
#    result = test.romanToInt(t)
#    print(result)