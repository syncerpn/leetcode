# similar to #2305, where we just brute-force with backtracking
# but we need several optimizations to not get tle
# such as eliminate duplicated assignments
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        workers = [0] * k
        
        ans = [sum(jobs)]
        # jobs.sort(reverse = True)
        def dfs(curr):
            if curr == len(jobs):
                ans[0] = min(ans[0], max(workers))
                return
            
            seen = set() # record searched workload of workers
            for i in range(k):
                if workers[i] in seen: continue # if we have searched the workload of 5, skip it.
                if workers[i] + jobs[curr] >= ans[0]: continue # another branch cutting
                seen.add(workers[i])
                workers[i] += jobs[curr]
                dfs(curr+1)
                workers[i] -= jobs[curr]
        
        dfs(0)
        return ans[0]