from typing import List

class Solution:
    # for n by m input array runs in
    # O(nm) time
    # O(m) space
    def numSpecial(self, mat: List[List[int]]) -> int:
        # First define a Array of length len(mat)
        width = len(mat[0]) #Width

        # Each store_unique[j] represents the number of 1's
        # in that column that are also the only one in their row
        store_unique = [0] * width

        # Each store_all[j] represents the number of 1's
        # in that column in total
        store_all = [0] * width
        
        # For each row in the matrix look for a
        # 1 that is the only one in the row
        for row in mat:
            last = -1
            count = 0
            for i in range(width):
                if row[i] == 1:
                    count = count + 1
                    last = i
                    store_all[i] = store_all[i] + 1
            if count == 1:
                # We have found the only 1
                # in the row.
                # note it's column in the storage array
                store_unique[last] = store_unique[last] + 1
        count = 0
        for i in range(width):
            if store_unique[i] == 1 == store_all[i]:
                count = count + 1
        return count

mat = [[0,1],
       [1,0]]

mat = [[0,0,0,0,0,1,0,0],
       [0,0,0,0,1,0,0,1],
       [0,0,0,0,1,0,0,0],
       [1,0,0,0,1,0,0,0],
       [0,0,1,1,0,0,0,0]]

print(Solution.numSpecial(None, mat))
                