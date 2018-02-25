class FindAnagramMappings:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        b_list = []
        for b in B:
            b_list.append(b)
        result_list = []
        for a in A:
            result_list.append(b_list.index(a))
        return result_list

    def anOptionalWay(self, A, B):
        d = {}
        for i, b in enumerate(B):
            if b not in d:
                d[b] = []
            d[b].append(i)
        return [d[a].pop() for a in A]

    def officialSolution(self, A, B):
        D = { d:i  for i,d in enumerate(B)}
        return [D[a] for a in A]

# pop() is O(1) while index() is O(N)


