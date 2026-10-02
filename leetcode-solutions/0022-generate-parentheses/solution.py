class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # This list will store all our finished, valid combinations
        result = []
        
        # A helper function that builds the brackets one by one
        def build_string(current_str, open_count, close_count):
            # Base Case: If the string reaches the perfect length (2 * n), we are done!
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            
            # Rule 1: Can we add an opening bracket '('?
            if open_count < n:
                build_string(current_str + "(", open_count + 1, close_count)
                
            # Rule 2: Can we add a closing bracket ')'?
            if close_count < open_count:
                build_string(current_str + ")", open_count, close_count + 1)
        
        # Start our helper function with an empty string and 0 counts
        build_string("", 0, 0)
        
        return result

