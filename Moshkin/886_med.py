class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        colors = [2 for i in range(n)]
        if not dislikes:
            return True
        queue = []
        pivot = 0
        # BFS
        # outer cycle between connectivity components
        while 2 in colors:
            ind = colors.index(2)
            queue.append(ind + 1)
            colors[ind] = 0
            # inner cycle in one connectivivty component
            while queue:
                pivot = queue.pop(0)
                for ed in dislikes:
                    if ed[0] == pivot:
                        if colors[ed[1] - 1] == 2:
                            queue.append(ed[1])
                            colors[ed[1] - 1] = 1 - colors[pivot - 1]
                        elif colors[ed[1] - 1] == colors[pivot - 1]:
                            return False
                    elif ed[1] == pivot:
                        if colors[ed[0] - 1] == 2:
                            queue.append(ed[0])
                            colors[ed[0] - 1] = 1 - colors[pivot - 1]
                        elif colors[ed[0] - 1] == colors[pivot - 1]:
                            return False
        return True
