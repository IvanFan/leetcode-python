class JewelsAndStones:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if not J:
            return 0
        elif not S:
            return 0
        elif len(S) == 0:
            return 0
        elif len(J) == 0:
            return 0

        dictOfJ = {}
        for jChar in J:
            dictOfJ[jChar] = True
        totalJewels = 0
        for sChar in S:
           if dictOfJ.get(sChar):
               totalJewels += 1
        return totalJewels

    def betterSolution(self, J, S):
        jSet = set(J)
        return sum(s in jSet for s in S)




