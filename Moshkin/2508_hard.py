class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: set() for i in range(1, n + 1)}
        # calculate nodes degrees
        for ed in edges:
            adj[ed[0]].add(ed[1])
            adj[ed[1]].add(ed[0])
        odd = [el[0] for el in adj.items() if len(el[1]) % 2 == 1]
        length = len(odd)
        if length == 0:
            return True
        elif length == 2:
            if odd[0] not in adj[odd[1]]:
                return True
            # search for node in graph who has not connection
            # between both of nodes having odd degree. 
            # -> if found then return true else return false
            if set([i for i in range(1, n + 1)]).difference(
                adj[odd[0]].union(adj[odd[1]]).union(
                    {odd[0], odd[1]}
                )
            ) != set():
                return True
        elif length == 4:
            # if odd subgraph is star
            if odd[1] in adj[odd[0]] and\
                    odd[2] in adj[odd[0]] and\
                    odd[3] in adj[odd[0]] or \
                odd[0] in adj[odd[1]] and \
                            odd[2] in adj[odd[1]] and \
                            odd[3] in adj[odd[1]] or \
                odd[0] in adj[odd[2]] and \
                            odd[1] in adj[odd[2]] and \
                            odd[3] in adj[odd[2]] or \
                odd[0] in adj[odd[3]] and \
                            odd[2] in adj[odd[3]] and \
                            odd[1] in adj[odd[3]]:
                return False
            # if 3 nodes connect to each other and last node is
            # isolated from their
            if odd[1] in adj[odd[0]] and odd[2] in adj[odd[0]] \
                    and odd[1] in adj[odd[2]] or \
                odd[2] in adj[odd[0]] and odd[3] in adj[odd[0]]\
                    and odd[2] in adj[odd[3]] or \
                odd[1] in adj[odd[0]] and odd[3] in adj[odd[0]]\
                    and odd[1] in adj[odd[3]] or \
                odd[0] in adj[odd[1]] and odd[2] in adj[odd[1]]\
                    and odd[0] in adj[odd[2]] or \
                odd[0] in adj[odd[1]] and odd[3] in adj[odd[1]]\
                    and odd[0] in adj[odd[3]] or \
                odd[2] in adj[odd[1]] and odd[3] in adj[odd[1]]\
                    and odd[2] in adj[odd[3]] or \
                odd[0] in adj[odd[2]] and odd[1] in adj[odd[2]]\
                    and odd[0] in adj[odd[1]] or \
                odd[0] in adj[odd[2]] and odd[3] in adj[odd[2]]\
                    and odd[0] in adj[odd[3]] or \
                odd[1] in adj[odd[2]] and odd[3] in adj[odd[2]]\
                    and odd[1] in adj[odd[3]] or \
                odd[0] in adj[odd[3]] and odd[1] in adj[odd[3]]\
                    and odd[0] in adj[odd[1]] or \
                odd[0] in adj[odd[3]] and odd[2] in adj[odd[3]]\
                    and odd[0] in adj[odd[2]] or \
                odd[1] in adj[odd[3]] and odd[2] in adj[odd[3]]\
                    and odd[1] in adj[odd[2]]:
                return False
            return True
        return False