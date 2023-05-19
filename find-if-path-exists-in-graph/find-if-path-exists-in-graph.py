from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjacent_list = [[] for _ in range(n)]
        for a,b in edges:
            adjacent_list[a].append(b)
            adjacent_list[b].append(a)
        
        queue = deque([source])
        seen = set([source])
        
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for neighbor in adjacent_list[node]:
                if neighbor not in seen:
                    queue.append(neighbor)
                    seen.add(neighbor)
                    
        return False
                    
                    