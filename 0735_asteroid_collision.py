# fairly easy with stack
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for a in asteroids:
            while s and s[-1] > 0 and a < 0:
                if s[-1] + a > 0:
                    break
                elif s[-1] + a == 0:
                    s.pop()
                    break
                else:
                    s.pop()
            else:
                s.append(a)
        return s