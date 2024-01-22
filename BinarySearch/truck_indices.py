import heapq

class Solution:
    def truck_indices(self, trucks, items):
        truck_items = trucks[:]
        heapq.heapify(trucks)
        result = []
        for i in range(len(items)):
            popped_element = heapq.heappop(trucks)

            while True: 
                if popped_element > items[i]:
                    # Get the index of the popped element
                    index_of_popped_element = truck_items.index(popped_element)
                    result.append(index_of_popped_element)
                    break
                else:
                    popped_element = heapq.heappop(trucks)

        return result
    
sol = Solution()
output = sol.truck_indices([4, 5, 7, 2], [1, 2, 5])
            