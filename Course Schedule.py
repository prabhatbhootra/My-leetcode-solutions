class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #0 -> 1 -> 2     #4 -> 5
             #|
             #V
             #3
        graph = {}
        for edge in prerequisites:
            if edge[1] not in graph:
                graph[edge[1]] = [edge[0]]
            else:
                graph[edge[1]].append(edge[0])
        self.seen = set()
        def isCyclic(node):
            if node in self.seen:
                return True
            else:
                self.seen.add(node)
                if node in graph.keys():
                    for course in graph[node]:
                        if isCyclic(course):
                            return True
            self.seen.remove(node)
            return False
        for i in range(0, numCourses):
            if isCyclic(i):
                return False
        return True
            
