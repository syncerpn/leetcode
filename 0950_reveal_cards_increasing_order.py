# simulate with queue/stack
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = [0] * len(deck)
        s = list(range(len(deck)))
        j = 0
        for c in deck:
            i = s.pop(j)
            result[i] = c
            if not s:
                break
            j = (j + 1) % (len(s))
        return result