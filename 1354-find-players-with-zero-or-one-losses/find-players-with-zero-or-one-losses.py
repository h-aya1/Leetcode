class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = []
        loss = []
        win = []
        los =[]
        for ls in matches:
            wins.append(ls[0])
            loss.append(ls[1])
        wins = Counter(wins)
        loss = Counter(loss)
        for val , freq in wins.items():
            if val not in loss:
                win.append(val)
        for value, count in loss.items():
            if loss[value] == 1:
                los.append(value)
        win.sort()
        los.sort()
        return [win,los]