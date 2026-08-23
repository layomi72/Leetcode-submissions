class Solution:

    def encode(self, strs: List[str]) -> str:
        str1 = ""
        for i in range (0,len(strs)):
            str1 += strs[i]
            str1 += "/./"
        return str1

    def decode(self, s: str) -> List[str]:
        string_list = s.split("/./")
        string_list.pop(-1)
        return string_list