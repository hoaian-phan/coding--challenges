class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        myStack = [source]
        seen = set()
        
        adjacent_list = [[] for _ in range(n)]
        for a, b in edges:
            adjacent_list[a].append(b)
            adjacent_list[b].append(a)
            
        while myStack:
            current = myStack.pop()
            if current == destination:
                return True
            if current not in seen:
                myStack.extend(adjacent_list[current])
                seen.add(current)
                
        return False
            
        
        