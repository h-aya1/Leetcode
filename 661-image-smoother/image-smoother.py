class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        img2 = [[0] * len(img[0]) for _ in range(len(img))]
    
        dxn = [(0,0) ,(-1,-1), (1,1), (1,-1), (-1,1), (0,1), (0,-1),(1,0), (-1,0)]
        def is_valid(r,c):
            return 0 <= r < len(img) and 0 <= c < len(img[0])

        for r in range(len(img2)):
            
            for c in range(len(img2[0])):

                tot = 0
                count = 0
                for i,j in dxn:
                    if is_valid(r+i,c+j):
                        print(img[r+i][c+j])
                        tot += img[r+i][c+j]
                        count += 1
                    
                
                img2[r][c] = tot // count

        return img2
                