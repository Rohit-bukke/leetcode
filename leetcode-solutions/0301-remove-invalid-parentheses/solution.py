from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(': count += 1
                elif char == ')':
                    if count == 0: return False
                    count -= 1
            return count == 0
            
        result = []
        visited = set([s])
        queue = deque([s])
        found = False
        
        while queue:
            curr = queue.popleft()
            
            if is_valid(curr):
                result.append(curr)
                found = True
                
            if found:
                continue
                
            for i in range(len(curr)):
                if curr[i] not in '()': continue
                next_state = curr[:i] + curr[i+1:]
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)
                    
        return result
