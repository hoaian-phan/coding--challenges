class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = []
        for ele in paths:
            if stack and ele == '..':
                stack.pop()
            elif ele == '.':
                continue
            elif ele and ele != '..':
                stack.append(ele)
        
        return '/' + '/'.join(stack)
            
       