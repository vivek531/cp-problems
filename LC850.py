from heapq import heappop, heappush
class Solution:
    def rectangleArea(self, rectangles) -> int:
        num = len(rectangles)
        events = set()
        for i in range(num):
            x1, y1, x2, y2 = rectangles[i]
            events.add(x1)
            events.add(x2)

        total_area = 0
        rectangles.sort(key = lambda x: (x[0], x[2]))
        heap = []
        events = sorted(list(events))
        index = 0
        for i in range(len(events)):
            current_x = events[i]
            if len(heap)!=0:
                height = self.merge(heap)
                width = (current_x-events[i-1]) % (10**9+7)
                total_area += height*width


            while index < num:
                x1, y1, x2, y2 = rectangles[index]
                if current_x == x1:
                    heappush(heap, (x2, y2, x1, y1))
                    index += 1
                else:
                    break
            
            while len(heap)!=0:
                x2, y2, x1, y1 = heappop(heap)
                if current_x == x2:
                    continue
                else:
                    heappush(heap, (x2, y2, x1, y1))
                    break
        
        return total_area % (10**9+7)
    
    def merge(self, heap):
        intervals = []
        for i in range(len(heap)):
            x2, y2, x1, y1 = heap[i]
            intervals.append([y1, y2])
        
        intervals.sort(key=lambda x: (x[0], x[1]))

        stack = [intervals[0]]
        index = 1
        while index < len(intervals):
            last = stack[-1]
            if last[1] <=  intervals[index][0]:
                stack.append(intervals[index])
                index += 1
            else:
                del stack[-1]
                interval = [min(last[0], intervals[index][0]), max(last[1], intervals[index][1])]
                stack.append(interval[:])
                index += 1
        
        length = 0
        for i in range(len(stack)):
            length += (stack[i][1]-stack[i][0])

        return length % (10**9+7)

solution = Solution()
output = solution.rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]])
print(output)