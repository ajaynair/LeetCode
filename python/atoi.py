import pdb

class Solution:
    def removeGarbage(self, string: str) -> str:
        if string is "":
            return ""

        pdb.set_trace()
        while string[0] == " ":
              string = string[1:]

        for c in string[::-1]:
            if c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return string
            string = string[:-1]

        return string

    def getSignAndAdjustStartChar(self, string: str) -> int:
        if string == "" or string is None:
            return None

        if string[0] == '-':
            string = string[1:]
            return -1, string
        if string[0] == '+':
            string = string[:1]
            return 1, string

        return 1, string

    def isValid(self, string: str) -> bool:
        if string[0] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return False
        return True

    def convertStrToInt(self, string: str):

        ans: int = 0

        for c in string:
            ans = ans * 10 + (ord(c) - ord('0'))

        return ans

    def myAtoi(self, s: str) -> int:
        s = self.removeGarbage(s)

        if s is None:
            return 0

        sign, s = self.getSignAndAdjustStartChar(s)

        is_valid = self.isValid(s)
        if not is_valid:
            return 0

        int_s = self.convertStrToInt(s)

        return int_s * sign

s = Solution()
print(s.myAtoi("4193 with words"))
