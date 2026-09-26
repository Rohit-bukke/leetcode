class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Build lookup table for O(1) key access
        lookup = {k: v for k, v in knowledge}
        
        res = []
        cur_key = []
        in_bracket = False
        
        for ch in s:
            if ch == '(':
                in_bracket = True
                cur_key = []
            elif ch == ')':
                in_bracket = False
                key_str = "".join(cur_key)
                res.append(lookup.get(key_str, '?'))
            else:
                if in_bracket:
                    cur_key.append(ch)
                else:
                    res.append(ch)
                    
        return "".join(res)
