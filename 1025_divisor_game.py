# proof is that, if we get an even number, you can always subtract 1 to make it odd for Bob
# when bob takes an odd, he can only find an odd divisor
# so we can be sure that he will send back an odd - odd = even number to Alice
# in the end, this reduces to 2 then 1, and Alice wins
# otherwise, Bob wins
class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0