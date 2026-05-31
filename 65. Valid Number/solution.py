class Solution:
    def isDecimalNumber(self, s: str) -> bool:
        if s == "":
            return False
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        substrs = s.split('.')
        if len(substrs) != 2:
            return False
        if substrs[0] == "":
            if substrs[1].isnumeric():
                return True
            else:
                return False
        elif substrs[0].isnumeric():
            return substrs[1] == "" or substrs[1].isnumeric()
        else:
            return False


    def isInteger(self, s: str) -> bool:
        if s == "":
            return False
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        return s.isnumeric()


    def isNumber(self, s: str) -> bool:
        s = s.lower()
        substrs = s.split('e')
        if len(substrs) == 1:
            return (
                self.isDecimalNumber(substrs[0]) or 
                self.isInteger(substrs[0])
            )
        elif len(substrs) == 2:
            return (
                self.isDecimalNumber(substrs[0]) or 
                self.isInteger(substrs[0])
            ) and self.isInteger(substrs[1])
        else:
            return False
