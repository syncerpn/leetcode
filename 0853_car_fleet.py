# sort cars by initial position
# calculate the time to arrive of each car
# add time to stack
# if a later car need less time to reach a target
# it will catch up a car fleet
# otherwise it will create a new car fleet
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [(p, s) for p, s in zip(position, speed)]
        ps.sort(reverse=True)
        stack = []
        for p, s in ps:
            t = (target - p) / s
            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)