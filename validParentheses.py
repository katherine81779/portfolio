class Solution:
    def isValid(self, s: str) -> bool:
        
        # This is an O(N) search to check if the given input is a valid way to check
        # the parentheses.
        # For example, "()", "()[]{}", "{[]}" will return true
        # But, "{[}" and "(]" will return false
        
        brackets = {'(':')', '{':'}', '(':')', '[':']'}
        
        # The stack will help keep track of the number of left parentheses
        stack = []
        
        if len(s) == 0: return True
        if len(s) % 2 == 1: return False
        for bracket in s:
            if bracket in brackets: #checks if it is a left bracket
                stack.append(bracket)
            else:
                if len(stack) == 0: return False 
                # returns False meaning there is an uneven number of matching parentheses
                closing = stack[len(stack) - 1]
                stack.pop()
                if bracket != str(brackets[closing]): return False
                # returns False because it was the incorrect matching parenthesis 
        if len(stack) != 0: return False 
        # returns False meaning there is an uneven number of matching parentheses
        return True
