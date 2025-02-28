class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []

        
        for size in range(len(arr), 1, -1):
            
            max_index = arr.index(max(arr[:size]))

            if max_index != size - 1:
  
                if max_index != 0:
                    result.append(max_index + 1)
                    arr[:max_index + 1] = reversed(arr[:max_index + 1])
                    
                result.append(size)
                arr[:size] = reversed(arr[:size])

        return result