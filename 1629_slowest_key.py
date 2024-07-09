# track max duration and character
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        d = releaseTimes[0]
        c = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            di = releaseTimes[i] - releaseTimes[i-1]
            ci = keysPressed[i]
            if di > d:
                d = di
                c = ci
            elif di == d and c < ci:
                c = ci
        
        return c
