# eventhough tagged "hard", this is one is fair easy
# 1-d navigation makes me think of stack immediately
# and it works beautifully
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        phdi = sorted(zip(positions, healths, directions, list(range(len(positions)))))
        stack_collision = []
        stack_safe = []
        
        for p, h, d, i in phdi:
            if d == "R":
                stack_collision.append([i, h])
            else:
                while stack_collision:
                    j, k = stack_collision[-1]
                    if k == h:
                        stack_collision.pop()
                        break
                    elif k < h:
                        stack_collision.pop()
                        h -= 1
                    else:
                        stack_collision[-1][1] -= 1
                        break
                else:
                    stack_safe.append([i,h])
        return [h for i, h in sorted(stack_collision + stack_safe)]
        