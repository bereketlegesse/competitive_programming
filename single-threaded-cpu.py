class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for i in range(n):
            tasks[i].append(i)
        
        tasks.sort()
        curTasks = []
        curTime = tasks[0][0]
        i = 0
        answer = []
        
        while i < n:
            flag = True
            while i < n and curTime >= tasks[i][0]:
                flag = False
                heapq.heappush(curTasks,(tasks[i][1],tasks[i][2]))
                i += 1

            if flag and not curTasks:
                curTime = tasks[i][0] 
                continue

            dur, idx = heapq.heappop(curTasks)
            answer.append(idx)
            curTime += dur
            
        while curTasks:
            dur, idx = heapq.heappop(curTasks)
            answer.append(idx)


        return answer