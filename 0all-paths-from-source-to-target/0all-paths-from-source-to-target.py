class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # The queue will store a list of (vertex, path)
        queue = collections.deque([(0, [0])])
        paths = []
        
        while queue:
            node, path = queue.popleft()
            if node == len(graph) - 1:
                paths.append(path)
            
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))
                
        return paths
                
                