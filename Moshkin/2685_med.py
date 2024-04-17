class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        conn_comp = [-1 for i in range(n)]
        num_cc = 0
        queue = []
        pivot = 0
        ind = 0
        num_edg = 0
        num_ver = 0
        # BFS
        # outer cycle between connectivity components
        while -1 in conn_comp:
            num_cc += 1
            ind = conn_comp.index(-1)
            queue.append(ind)
            num_ver = 1
            num_edg = 0
            conn_comp[ind] = num_cc
            # inner cycle in one connectivivty component
            while queue:
                pivot = queue.pop(0)
                for i, ed in enumerate(edges[::-1]):
                    if ed[0] == pivot:
                        if conn_comp[ed[1]] == -1:
                            queue.append(ed[1])
                            num_ver += 1
                        num_edg += 1
                        conn_comp[ed[1]] = num_cc
                        edges.remove(ed)
                    elif ed[1] == pivot:
                        if conn_comp[ed[0]] == -1:
                            queue.append(ed[0])
                            num_ver += 1
                        num_edg += 1
                        conn_comp[ed[0]] = num_cc
                        edges.remove(ed)
            # connectivity component was fully explored
            if num_ver * (num_ver - 1) / 2 != num_edg:
                num_cc = max(num_cc - 1, 0)
        return num_cc