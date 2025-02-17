class Solution:
    def frequencySort(self, s: str) -> str:
        
        result = ""
        freq_dict = Counter(s)  

        freq_list = []

        for char, count in freq_dict.items():
            freq_list.append((char, count))  
        
        freq_list.sort(key=lambda pair: pair[1], reverse=True)  

        
        for char, count in freq_list:
            result += char * count  

        
        return result