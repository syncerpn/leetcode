#1. need to count first
#2. as forming hands, recount the remaining cards
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand_dict = {}
        for i in hand:
            if i not in hand_dict:
                hand_dict[i] = 0
            hand_dict[i] += 1
        
        for i in sorted(hand_dict.keys()):
            n = hand_dict[i]
            if n == 0:
                continue
            for j in range(1,groupSize):
                if i+j not in hand_dict:
                    return False
                if hand_dict[i+j] < n:
                    return False
                hand_dict[i+j] -= hand_dict[i]        
        return True