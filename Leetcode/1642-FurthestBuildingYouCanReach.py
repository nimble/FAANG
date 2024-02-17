class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        N = len(heights)-1
        jumps = 0 
        heap = []
        for i in range(N):
            diff = heights[i+1] - heights[i]

            if diff <=0:
                continue
            
            # We're going to store the difference into the maxheap to keep track of the differences as long as the difference isn't 0.
            bricks-=diff
            heapq.heappush(heap, -diff)

            # Let's use our ladders since we've run out of bricks
            if bricks < 0:
                if ladders == 0:
                    return i
                # Use a ladder
                ladders-=1
                # Since we've used a ladder, why not add the largest difference back into the bricks?
                bricks+= -heapq.heappop(heap)
        
        return len(heights) - 1





            # # if any of our bricks or ladders finish in supply, we simply return the jumps we've made.
            # if (bricks == 0 and ladders == 0):
            #     return jumps
            # # If the current spot we're at is higher than the next height, we can safely make a jump.
            # if(heights[i] >= heights[i+1]):
                
            # else:
            #     # If the next height is larger than our current, we need to utilize our supply starting with bricks.
            #     if(bricks + heights[i] >= heights[i+1]):
            #         if(bricks - (heights[i+1] - heights[i]) >= 0):
            #             bricks -=(heights[i+1] - heights[i])
            #             # print("Remaining Bricks:", bricks)
            #             jumps+=1
            #     else:
            #         # If our brick is finished, we can use our ladders to get to next building.
            #         ladders-=1
                    
        return jumps

        
