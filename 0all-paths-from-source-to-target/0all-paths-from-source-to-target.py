class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        myStack = [(0, [0])]  # Each element in the stack is a tuple containing (current node, current path)
        paths = []

        while myStack:
            current, path = myStack.pop()

            if current == len(graph) - 1:
                paths.append(path)

            for neighbor in graph[current]:
                myStack.append((neighbor, path + [neighbor]))

        return paths
                