#-------Problem: 1834--------


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for index, task in enumerate(tasks):
            task.append(index)
        tasks.sort(key = lambda t: t[0])

        res, minHeap = [], []
        i, time = 0, tasks[0][0]

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if not minHeap:
                time = tasks[i][0]
            else:
                procTime, index = heappop(minHeap)
                time += procTime
                res.append(index)

        return res