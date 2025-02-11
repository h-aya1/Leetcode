class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = []
        
        chars = Counter(chars)
        # Counter({'a': 2, 't': 1, 'c': 1, 'h': 1})
        for word in words:

            word = Counter(word)
            tmp = []
            for val , con in word.items():
                
                if chars[val] >= word[val]:
                    tmp.append(word[val])
                else:
                    break

            if len(word) == len(tmp):
                ans.extend(tmp) 

        return sum(ans)