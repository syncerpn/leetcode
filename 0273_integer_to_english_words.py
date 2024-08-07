# not difficult
# just burdensome
class Solution:
    def numberToWords(self, num: int) -> str:
        d = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
            5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
            20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
            60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety",
            100: "Hundred", 1000: "Thousand", 1000000: "Million", 1000000000: "Billion"
        }

        def name_group(n):
            r = []
            h = n // 100
            t = n % 100
            if h > 0:
                r.append(d[h] + " " + d[100])
            if t >= 20:
                r.append(d[t // 10 * 10])
                u = t % 10
                if u > 0:
                    r.append(d[u])
            elif t > 0:
                r.append(d[t])
            return " ".join(r) if r else ""

        if num == 0:
            return d[0]
        
        ans = []
        b = name_group(num // 1000000000)
        if b:
            ans.append(b + " " + d[1000000000])
        
        num = num % 1000000000
        m = name_group(num // 1000000)
        if m:
            ans.append(m + " " + d[1000000])
        
        num = num % 1000000
        t = name_group(num // 1000)
        if t:
            ans.append(t + " " + d[1000])
        
        num = num % 1000
        u = name_group(num)
        if u:
            ans.append(u)

        print(ans)
        return " ".join(ans)