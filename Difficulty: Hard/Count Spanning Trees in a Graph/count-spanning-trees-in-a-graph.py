import numpy as np


class Solution:
    def countSpanTree(self, n, edges):
        lst = np.zeros((n, n, ))
        
        for sta, sto in edges:
            lst[sta][sta]+=1
            lst[sto][sto]+=1
            lst[sta][sto]-=1
            lst[sto][sta]-=1
            
        lr = lst[:-1, :-1]
        
        return round(np.linalg.det(lr))
        