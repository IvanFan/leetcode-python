class Solution:
    res=[]
    mar=0
    nn=0
    def fillInArray(self, list, index, value):
        list[index]=value
        if index == (self.mar-1):
            if sum(list)==self.nn:
                print(list[:])
                self.res.append(list[:])
            return 0
        else:
            if value < 9:
                for j in range(index+1, self.mar):
                    list[j]=0
                for x in range(value+1, 10):
                    self.fillInArray(list, index+1, x);

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res=[]
        if k==0 or n==0:
            return []
        if k > 9:
            return []
        tem=0
        for t in range(9,9-k,-1):
            tem += t
        if tem < n:
            return []
        tem=0
        for t in range(1,k+1):
            tem += t
        if tem >  n:
            return []
        list=[0]*k
        index=0
        self.mar=k
        self.nn=n
        for x in range(1, 10):
            self.fillInArray(list, index, x)
        return self.res
