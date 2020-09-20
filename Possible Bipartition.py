class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if len(dislikes) == 0:
            return True
        graph = {}
        for edge in dislikes:
            if edge[0] not in graph.keys():
                graph[edge[0]] = [edge[1]]
            else:
                graph[edge[0]].append(edge[1])
            if edge[1] not in graph.keys():
                graph[edge[1]] = [edge[0]]
            else:
                graph[edge[1]].append(edge[0])
        colors = {}
        def dfs(node, color):
            if node not in colors:
                colors[node] = color
            else:
                return colors[node] == color
            if node in graph:
                for dislike in graph[node]:
                    if not dfs(dislike, 1 - color):
                        return False
            return True
        for i in range(1, N+1):
            if i not in colors and not dfs(i, 0):
                return False
        return True
