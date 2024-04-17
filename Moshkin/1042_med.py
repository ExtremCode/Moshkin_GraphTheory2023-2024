class Solution:
    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
        # Wales Powell's algorithm without
        # ordering the vertices' degrees
        colors = [-1 for i in range(n)]
        adj = {i: set() for i in range(1, n + 1)}
        # set up the lists of adjacent
        for ed in paths:
            adj[ed[0]].add(ed[1])
            adj[ed[1]].add(ed[0])
        num_col = 0
        # block is set that contains adjacent vertices with
        # a set of painted 
        block = set()
        while -1 in colors:
            num_col += 1
            pivot = colors.index(-1) + 1
            colors[pivot - 1] = num_col
            block = block.union(adj[pivot])
            for ind, w in enumerate(colors):
                if w == -1 and (ind + 1) not in block:
                    colors[ind] = num_col
                    block = block.union(adj[ind + 1])
            block.clear()
        return colors