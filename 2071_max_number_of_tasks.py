# beautiful solution with optimized runtime using deque
# use binary search to search for the max amount of tasks, instead of designing a strategy and counting assignment
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        def can_assign(k):
            if k == 0:
                return True

            task_temp = deque()
            pm = pills
            t = 0
            # try to assign k smallest tasks to top k strongest workers
            for w in workers[-k:]:
                # with each worker, looking for the appropriate tasks, also considering when a pill is taken
                task_threshold = w + strength if pm else w
                while t < k and tasks[t] <= task_threshold:
                    task_temp.append(tasks[t])
                    t += 1
                
                # if no task can be assigned, trial failed
                if len(task_temp) == 0:
                    return False

                if w >= task_temp[0]: # either, we assign the smallest task if not taking pill
                    task_temp.popleft()
                elif pm: # or, we assign the biggest possible one if pill is taken
                    task_temp.pop()
                    pm -= 1
                else: # if we need pill, but not having one to use
                    return False
            
            return True

        tasks.sort()
        workers.sort()

        l, r = 0, min(len(tasks), len(workers)) + 1
        while l + 1 < r:
            k = (l + r) // 2
            if can_assign(k):
                l = k
            else:
                r = k
        
        return l