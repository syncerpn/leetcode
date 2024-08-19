# was not that hard until 7 appeared, lol
# my approach was good and almost solved it during the contest
# but in the end, i failed
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if k == 1:
            return "9" * n

        if k == 2:
            if n < 3:
                return "8" * n
            return "8" + "9" * (n - 2) + "8"

        if k == 3 or k == 9:
            return "9" * n

        if k == 4:
            if n < 5:
                return "8" * n
            return "88" + "9" * (n - 4) + "88"
        
        if k == 5:
            if n < 3:
                return "5" * n
            return "5" + "9" * (n - 2) + "5"
        
        if k == 6:
            if n < 3:
                return "6" * n
            if n == 3:
                return "888"
            if (n - 3) % 2 == 0:
                return "8" + "9" * ((n - 3) // 2) + "8" + "9" * ((n - 3) // 2) + "8"
            return "8" + "9" * ((n - 4) // 2) + "77" + "9" * ((n - 4) // 2) + "8"
        
        if k == 8:
            if n < 7:
                return "8" * n
            return "888" + "9" * (n - 6) + "888"

        if k == 7:
            dic = {0: '', 1: '7', 2: '77', 3: '959', 4: '9779', 5: '99799', 6: '999999', 7: '9994999',
                       8: '99944999', 9: '999969999', 10: '9999449999', 11: '99999499999'}
            l, r = divmod(n, 12)
            return '999999' * l + dic[r] + '999999' * l