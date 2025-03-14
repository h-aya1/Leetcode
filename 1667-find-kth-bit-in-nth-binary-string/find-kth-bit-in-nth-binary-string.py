class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def str_sn(n):
            if n == 1:
                return "0"

            return str_sn(n-1) + "1" + self.invert(str_sn(n-1))[::-1]

        return str_sn(n)[k-1]

    def invert(self, x):

        x = list(x)

        for i in range(len(x)):

            if x[i] == "1":

                x[i] = "0"

            else:

                x[i] = "1"

        return "".join(x)
        


        
        
