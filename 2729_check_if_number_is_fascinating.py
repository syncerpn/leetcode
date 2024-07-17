# small input
# so just utilize lib to make it compact
class Solution:
    def isFascinating(self, n: int) -> bool:
        print(sorted(str(n) + str(n*2) + str(n*3)))
        return "".join(sorted(str(n) + str(n*2) + str(n*3))) == "123456789"