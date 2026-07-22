# same as #0316
# greedy
# we build an increasing char monostack
# iterate current char c of s
# if the top of the stack is lexico larger than c and will appear again, pop it out of the stack
# and append c into the top
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = Counter(s)
        seen = set()
        stack = []

        for c in s:
            freq[c] -= 1
            if c in seen: continue

            while stack and stack[-1] > c and freq[stack[-1]]:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)

        return "".join(stack)
        