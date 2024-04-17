class Solution:
    def dfs(self, vert, visited, adj):
        visited.add(vert)
        for el in adj[vert]:
            if el not in visited:
                self.dfs(el, visited, adj)
    
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        adj = [set() for i in range(n)]
        visited = set()
        for ed in edges:
            adj[ed[0]].add(ed[1])
            adj[ed[1]].add(ed[0])
        prev_ln = 0
        res = n*(n - 1)//2
        # recursive DFS with counting nodes in 
        # each connectivity component
        for i in range(n):
            if i not in visited:
                self.dfs(i, visited, adj)
            ln = len(visited)
            res -= (ln - prev_ln)*(ln - prev_ln - 1)//2
            prev_ln = ln
        return res