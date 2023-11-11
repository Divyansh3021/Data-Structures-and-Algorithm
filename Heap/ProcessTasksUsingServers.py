#-------Process: 1882-------

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = [0] * len(tasks)

        available = [(servers[i], i) for i in range(len(servers))]
        heapify(available)

        unavail = []
        time = 0
        for i in range(len(tasks)):
            time = max(time, i)

            if not available:
                time = unavail[0][0]
            while unavail and time >= unavail[0][0]:
                timefree, weight, index = heappop(unavail)
                heappush(available, (weight, index))
            
            weight, index = heappop(available)
            heappush(unavail, (time + tasks[i], weight, index))
            res[i] = index
        return res