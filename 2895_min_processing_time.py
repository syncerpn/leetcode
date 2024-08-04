# sort then greedily assign
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        for i in range(len(processorTime)):
            processorTime[i] += max(tasks[i*4:i*4+4])
        return max(processorTime)