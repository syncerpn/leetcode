# easy
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort(reverse=True)
        while asteroids:
            a = asteroids.pop()
            if mass < a:
                return False
            mass += a
        return True