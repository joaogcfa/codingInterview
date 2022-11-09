class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        visited = [0] * numCourses
        res = []
        for i in range(numCourses):
            if not self.dfs(graph, visited, i, res):
                return []
        return res

    def dfs(self, graph, visited, i, res):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        for j in graph[i]:
            if not self.dfs(graph, visited, j, res):
                return False
        visited[i] = 1
        res.append(i)
        return True
